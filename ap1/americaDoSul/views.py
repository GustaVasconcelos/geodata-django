from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request,"americaDoSul/index.html")

def brasil(request):
    return render(request,"americaDoSul/brasil.html")

def argentina(request):
    return render(request,"americaDoSul/argentina.html")

