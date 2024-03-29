"""DjangoAdvanced URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import ProductView,ProductImageView
from rest_framework_nested import routers
from app import views

router=routers.DefaultRouter()
router.register('product',ProductView,basename="product")


nested_router=routers.NestedDefaultRouter(router,'product',lookup='product_id')
nested_router.register('images',ProductImageView,basename="product-images")

urlpatterns = [
    path('index/',views.index,name="index"),
    path('',include(router.urls)),
    path('',include(nested_router.urls)),
    
    
] 