from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    api_url = 'http://localhost:8000/allData/'
    response = requests.get(api_url)
    data = response.json()

    context = {'data': data}

    return render(request, "validate/index.html", context)

def detail(request, url_path):
    print(url_path)
    api_url = f'http://127.0.0.1:8000/getData/?url_path=/{url_path}'
    response = requests.get(api_url)
    data = response.json()

    # Menyediakan data ke template
    context = {'data': data}

    return render(request, 'validate/detail.html', context)

@api_view(['POST'])
def validateJson(request):
    api_url = 'http://127.0.0.1:8000/validate_json/'
    response = requests.get(api_url)
    data = response.json()

    context = {'data': data}

    return render(request, 'validate/detail.html', context)
