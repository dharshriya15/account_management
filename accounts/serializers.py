from rest_framework import serializers
from .models import Account, Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'url', 'name']

class AccountSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'name', 'email', 'app_secret_token', 'destinations']