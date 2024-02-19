from rest_framework import serializers
from .models import Product,ProductImage
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=['id','image']
        
    def validate(self, attrs):
        print(attrs.get('file'))
        
    def create(self, validated_data):
        product_id=self.context['product_id']
        return ProductImage.objects.create(product_id=product_id,**validated_data)
class ProductSerializer(serializers.ModelSerializer):
    images=ProductImageSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields=['id','title','slug','description','price','inventory','last_update','images']