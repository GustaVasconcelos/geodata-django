from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request,"africa/index.html")

def marrocos(request):
    return render(request,"africa/marrocos.html")

def nigeria(request):
    return render(request,"africa/nigeria.html")

def gana(request):
    return render(request,"africa/gana.html")
