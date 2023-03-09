from rest_framework import serializers

from .models import Package, Subscription

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ("id", "title", "SKU", "description", "avatar", "price", "duration")

class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ("package", "created_time", "expire")