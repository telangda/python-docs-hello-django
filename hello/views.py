from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi Shivani, good morning, we are learning AZURE Cloud Computing & its very interesting ~!! ")
