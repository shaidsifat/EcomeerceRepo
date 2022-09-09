from .models import product,Order
from rest_framework import serializers
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"       