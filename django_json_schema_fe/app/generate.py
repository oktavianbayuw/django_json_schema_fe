from django.shortcuts import render

def index(request):
    return render(request, "generate/index.html")


def insert_data(request):
    return render(request, "generate/index.html")
