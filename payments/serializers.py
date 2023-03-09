from rest_framework import serializers

from .models import GateWay

class GatewaySerializer(serializers.ModelSerializer):

    class Meta:
     model = GateWay
     fields = ("id", "title", "description", "avatar")