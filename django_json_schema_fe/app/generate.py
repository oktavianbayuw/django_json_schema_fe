from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, "generate/index.html")

@csrf_exempt
def generate_json_schema(request):
    if request.method == 'POST':
        try:
            # Dapatkan data dari permintaan POST
            data = json.loads(request.body.decode('utf-8'))

            # Lakukan permintaan ke endpoint API
            api_url = "http://api-python.digitalevent.id/generateJsonSchema/"
            response = requests.post(api_url, json=data)

            # Periksa apakah permintaan berhasil
            if response.status_code == 200:
                # Jika berhasil, kembalikan respons dari API
                return JsonResponse(response.json())

            # Jika permintaan gagal, kembalikan pesan kesalahan
            return JsonResponse({'error': 'Failed to generate JSON Schema.'}, status=response.status_code)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

def insert_data(request):
    if request.method == 'POST':
        print("OK")
        url_path = request.POST.get('url_path')
        json_string = request.POST.get('json_string')
        json_schema = request.POST.get('json_schema')

        form_data = {
            'url_path': url_path,
            'json_string': json_string,
            'json_schema': json_schema
        }

        api_url = 'http://api-python.digitalevent.id/insertJson/'
        response = requests.post(api_url, data=form_data)
        print(response)
        if (response.status_code == 200 | response.status_code == 201):
            print(response.status_code)
            data = response.json()
            print(data)
            return render(request, "generate/index.html", {'data' : data})
        else:
            error_message = f"Error: {response.status_code} - {response.text}"
            return render(request, "generate/index.html", {'error_message': error_message})

    return render(request, "generate/index.html")

def fetch_api_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post('http://api-python.digitalevent.id/generateJsonSchema/')

        if response.status_code == 200:
            api_data = response.json()
            return JsonResponse(api_data)

        else:
            return JsonResponse({"error": "Failed to fetch API data"})