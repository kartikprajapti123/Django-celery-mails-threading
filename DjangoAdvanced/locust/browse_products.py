from locust import HttpUser,task,between
from random import randint


class WebsiteUser(HttpUser):
    wait_time=between(1,5)
    # @task(1)
    # def view_products(self):
    #     print("hello view")
    #     collection_di=randint(120,30)
    #     self.client.get(
    #         f'/shopdetails/?id={collection_di}',
    #         name='/product/')
        
    @task(2) 
    def view_product(self):
        print("thats it now after it we will move to another function in django ")
        print("hello view2")
        print("this is the way we can do all that the things")
        product_id=randint(120,130)
        self.client.get(f'/shopdetails/{product_id}')
        