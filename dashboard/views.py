from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    """ Render the page when the user is auth."""
    return HttpResponse("<h1>Dashboard</h1>")
