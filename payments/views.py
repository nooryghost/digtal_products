import uuid
import requests
from datetime import timezone 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import GateWay, Payment
from .serializers import GatewaySerializer
from subscriptions.models import Package, Subscription

class GatewayView(APIView):

    def get(self, request):
        gateways = GateWay.objects.filter(is_enable=True)
        serializer = GatewaySerializer(gateways, many=True)

        return Response(serializer.data)

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gateway_id = request.query_params.get("gateway")
        package_id = request.query_params.get("package")

        try:
            package = Package.objects.get(pk=package_id, is_enable=True)
            gateway = GateWay.objects.get(pk=gateway_id, is_enable=True)
        
        except (Package.DoesNotExist, GateWay.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        payment =Payment.objects.create(
            user=request.user,
            package=package,
            gateway=gateway,
            price=package.price,
            phone_number=request.user.phone_number,
            token=str(uuid.uuid4())
        )

        return Response({"token": payment.token, "callback_url": "https://my-site.com/payments/pay/"})

    def post(self, request):
        token = request.data.get("token")
        st = request.data.get("status")

        try:
            payment = Payment.objects.get(token=token)

        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if st != 10:
            payment.status = Payment.STATUS_CANCELED
            payment.save()

            return Response({"detail": "Payment verification failed"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        r = requests.post("bank_verify_url", data={})
        if r.status_code // 100 != 2:
            payment.status = Payment.STATUS_ERROR
            payment.save()

            return Response({"detail": "Payment verification failed"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        payment.status = Payment.STATUS_PAID
        payment.save()

        Subscription.objects.create(
            user=payment.user,
            package=payment.package,
            expire_time=timezone.now() + timezone.timedelta(days=payment.package.duration.days)
        )

        return Response()