from django.shortcuts import render
from django.http import JsonResponse
from .models import Product,ProductImage
from app.serializer import ProductImageSerializer,ProductSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail,EmailMessage
from templated_mail.mail import BaseEmailMessage
from rest_framework.throttling import AnonRateThrottle
from django.template.loader import render_to_string
# Create your views here.
from django.core.cache import cache
import requests



from app.tasks import MailSending
from .thread import *
def index(request):
    requests.get('https://httpbin.org/delay/2')
    if cache.get('httpbin_result') is None:
        response=requests.get('http://httpbin.org/delay/2')
        data=response.json()
        cache.set('httpbin_result',data)
    Send=MailSending.delay('mysterious.stories1234@gmail.com')
    print(Send)
    
    message=BaseEmailMessage(
        template_name='email.html',
        context={
            'name':'my name is kartik'
        }
    )
    message.send(['mysterious.stories1234@gmail.com'])
    
    
    subject="Message from kartik"
    message="Hello this is messag test"
    sender="kartikprajapati26122004@gmail.com"
    to="mysterious.stories1234@gmail.com"
    send_mail(
        subject,message,sender,[to]
    )
    
    # this is for sending mail with file attachment 
    
    email_template=render_to_string('email.html', {'name': 'my name is kartik'})
    message=EmailMessage('subject',email_template,'kartikprajapati2612004@gmail.com',['mysterious.stories1234@gmail.com'])
    message.attach_file('static/toymultiple.jpg')
    message.send()
    
    
    
    threads=threading.Thread(run()) 
    threads.start()
    
    return render(request,"index.html")


class ProductView(ModelViewSet):
    queryset=Product.objects.prefetch_related('images').all()
    serializer_class=ProductSerializer
    throttle_classes=[AnonRateThrottle]
    
    
class ProductImageView(ModelViewSet):
    serializer_class=ProductImageSerializer
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_id_pk']}

    def get_queryset(self):
        print(self.kwargs)
        return ProductImage.objects.filter(product_id=self.kwargs['product_id_pk'])
        
