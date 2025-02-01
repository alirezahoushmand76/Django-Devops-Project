from django.urls import path
from devopsdjango.blog.apis.products import ProductApi

urlpatterns = [
    path('product/', ProductApi.as_View(), name="product"),
]
