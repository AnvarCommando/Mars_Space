from rest_framework import serializers
from .models import *



class ProductSRL(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class OrderSRL(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'