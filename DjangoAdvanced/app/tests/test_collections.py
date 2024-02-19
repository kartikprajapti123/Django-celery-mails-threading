from rest_framework.test import APIClient
from rest_framework import status
import requests
from django.core.cache import cache

class TestCreateCollection:
    
    def test_if_user_is_anonymous_returns_401(self):
        # arrange
        
                
        client=APIClient()
        response=client.post('/product/',{'title':"hello my name isk aksrtik","slug":"dsd","price":10,"inventory":10})
        
        assert response.status.code==status.HTTP_401_UNAUTHORIZED
        
        
    @locals
    def say_helllo(self):
        exit()