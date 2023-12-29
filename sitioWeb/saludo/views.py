from django.shortcuts import render
from django.http import HttpResponse

def servicio(request):
    return HttpResponse("index")