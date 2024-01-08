from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import re
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    api_url = 'http://api-python.digitalevent.id/allData/'
    response = requests.get(api_url)
    data = response.json()

    context = {'data': data}

    return render(request, "validate/index.html", context)

def detail(request, url_path):
    print(url_path)
    api_url = f'http://api-python.digitalevent.id/getData/?url_path=/{url_path}'
    response = requests.get(api_url)
    data = response.json()

    context = {'data': data}

    return render(request, 'validate/detail.html', context)

@api_view(['POST'])
def validateJson(request):
    json_schema = request.data.get('json_schema')
    json_schema_remove_quote = remove_quotes_around_keys(json_schema)
    url_path = request.data.get('url_path')
    json_string = request.data.get('json_string')

    api_url = 'http://api-python.digitalevent.id/validate_json/'
    payload = {
        'json_schema': json_schema,
        'url_path': url_path,
        'json_string': json_string,
    }

    response = requests.post(api_url, json=payload)

    return Response(response.json())

def remove_quotes_around_keys(json_str):
    matches = re.findall(r'"(\w+)":', json_str)

    for match in matches:
        json_str = json_str.replace(f'"{match}":', f'{match}:')

    return json_str

def transform_json_format(json_str):
    json_str = re.sub(r'(\w+):', r'\1: ', json_str)

    json_str = re.sub(r'"(\w+)":', r'\1: ', json_str)

    return json_str

@csrf_exempt
def delete_data(request, url_path):
    if request.method == 'DELETE':
        try:
            # post to delete data url in backend
            api_url = f"http://api-python.digitalevent.id/delete/{url_path}/"
            print(api_url)
            response = requests.delete(api_url)

            if response.status_code == 200:
                return JsonResponse(response.json())

            return JsonResponse({'error': 'Failed to delete data.'}, status=response.status_code)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
    