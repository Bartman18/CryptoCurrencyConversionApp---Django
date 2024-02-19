from django.urls import path
from .views import  home, conversion, get_price,get_crypto_price,get_crypto_data,get_crypto_list

urlpatterns = [
    path("home/", home, name="home"),
    path("conversion/", conversion, name="conversion"),
    path("api/list", get_crypto_list, name="get_crypto_list"),
    path("api/data", get_crypto_data, name="get_crypto_data"),
    path("api/price", get_crypto_price, name="get_crypto_price"),
    path("api/<str:coin>/<str:currency>/price", get_price, name="get_price"),
]