from rest_framework import serializers

from galaksiya_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['prod_id','title','image_uri','productCategory','datePublished']