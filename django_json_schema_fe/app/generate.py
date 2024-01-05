from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def index(request):
    return render(request, "generate/index.html")


def insert_data(request):
    # Cek apakah request adalah POST
    if request.method == 'POST':
        # Ambil data dari formulir POST
        url_path = request.POST.get('url_path')
        json_string = request.POST.get('json_string')
        json_schema = request.POST.get('json_schema')

        # Formulir data untuk dikirim ke API
        form_data = {
            'url_path': url_path,
            'json_string': json_string,
            'json_schema': json_schema
        }

        # Ganti URL API sesuai dengan kebutuhan Anda
        api_url = 'http://localhost:8000/insertJson/'
        # Kirim permintaan POST ke API dengan data yang dikirim dari formulir
        response = requests.post(api_url, data=form_data)
        # Cek apakah permintaan berhasil
        if (response.status_code == 200 | response.status_code == 201):
            print(response.status_code)
            # Jika berhasil, dapatkan data respons dari API
            data = response.json()

            # Kirim data ke template
            return render(request, "generate/index.html")
        else:
            # Jika permintaan tidak berhasil, atur pesan kesalahan atau tindakan yang sesuai
            error_message = f"Error: {response.status_code} - {response.text}"
            return render(request, "generate/index.html", {'error_message': error_message})

    # Jika request bukan POST, kembalikan halaman biasa
    return render(request, "generate/index.html")

def fetch_api_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post('http://127.0.0.1:8000/generateJsonSchema/')

        if response.status_code == 200:
            api_data = response.json()
            return JsonResponse(api_data)

        else:
            return JsonResponse({"error": "Failed to fetch API data"})