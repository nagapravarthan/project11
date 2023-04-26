from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def welcome(request):
    res=HttpResponse("<html><body bgcolor=cyan ><h1><center>welcome to naga</center></h1></body><html>")
    return res