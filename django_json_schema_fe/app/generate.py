from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request, "generate/index.html")

@csrf_exempt
@api_view(['POST'])
def generate_json_schema(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            api_url = "http://api-python.digitalevent.id/generateJsonSchema/"
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                return JsonResponse(response.json())

            return JsonResponse({'error': 'Failed to generate JSON Schema.'}, status=response.status_code)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@api_view(['POST'])
def insert_data(request):
    
        json_schema = request.data.get('json_schema')
        url_path = request.data.get('url_path')
        json_string = request.data.get('json_string')

        api_url = 'http://api-python.digitalevent.id/insertJson/'
        payload = {
            'json_schema': json_schema,
            'url_path': url_path,
            'json_string': json_string,
        }

        response = requests.post(api_url, data=payload)
        print(response)
        if response.status_code == 201:
            return Response({'message' : 'success'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': f'Failed to insert data. Status code: {response.status_code}'})




def fetch_api_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post('http://api-python.digitalevent.id/generateJsonSchema/')

        if response.status_code == 200:
            api_data = response.json()
            return JsonResponse(api_data)

        else:
            return JsonResponse({"error": "Failed to fetch API data"})