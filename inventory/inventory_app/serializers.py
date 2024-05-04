from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['prod_name', 'prod_id', 'prod_price', 'prod_mfd', 'prod_quan', 'prod_supplier']

