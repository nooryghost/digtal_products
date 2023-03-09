from rest_framework.views import APIView

from .models import GateWay, Payment

class GatewayView(APIView):

    def get(self, request):
        gateways = GateWay.objects.filter(is_enable=True)
        serializer =

