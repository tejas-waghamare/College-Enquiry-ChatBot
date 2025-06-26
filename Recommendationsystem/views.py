from django.shortcuts import render
from django.http import HttpResponse

def viewuser(request):
    return HttpResponse("User view working!")
