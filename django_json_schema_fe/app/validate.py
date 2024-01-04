from django.shortcuts import render
import requests

def index(request):
    api_url = 'http://localhost:8000/allData/'
    response = requests.get(api_url)
    data = response.json()

    context = {'data': data}

    return render(request, "validate/index.html", context)

def insert_data(request):
    return render(request, "generate/index.html")
