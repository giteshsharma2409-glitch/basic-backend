from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Django Basic Backend")

def about(request):
    return HttpResponse("This is the About endpoint")

def api_data(request):
    return JsonResponse({
        "message": "This is a JSON response",
        "status": "success"
    })

def user_data(request):
    return JsonResponse({
        "id": 1,
        "name": "Gitesh",
        "course": "B.Tech CSE"
    })