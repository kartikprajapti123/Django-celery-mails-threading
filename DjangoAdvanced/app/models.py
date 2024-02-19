from django.db import models
from app.validators import validate_file_size
class Product(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    description=models.TextField(null=True,blank=True)
    price=models.IntegerField()
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title

# Create your models here.
class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images",default="")
    image=models.ImageField(upload_to='images',validators=[validate_file_size],)
    