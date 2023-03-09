from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Package, Subscription
from .serializers import PackageSerializer, SubscriptionSerializer

class PackageView(APIView):

    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)

        return Response(serializer.data)

class SubscriptionView(APIView):

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)

        return Response(serializer.data)