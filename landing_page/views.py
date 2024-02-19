from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """landing page view"""
    return HttpResponse("landing page")
