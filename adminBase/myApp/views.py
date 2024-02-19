from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def conversion(request):
    return render(request, 'conversionApp.html')


from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests

@require_http_methods(["GET"])
def get_crypto_list(request):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"

    response = requests.get(url)
    crypto_data = response.json()

    result_data = []
    for crypto in crypto_data:
        result_data.append({
            'name': crypto['name'],
            'symbol': crypto['symbol'],
            'price': crypto['current_price'],
            'image': crypto['image'],
        })

    return JsonResponse(result_data, safe=False)

@require_http_methods(["GET"])
def get_crypto_data(request):
    # Implement logic similar to the Spring Boot getCryptoList() method
    pass

@require_http_methods(["GET"])
def get_crypto_price(request):
    # Implement logic similar to the Spring Boot getPrice() method
    pass

@require_http_methods(["GET"])
def get_price(request, coin, currency):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    response = requests.get(api_url)
    return JsonResponse(response.json(), safe=False)