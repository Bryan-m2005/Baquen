from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de la app2</h1>")

def function(request):
    html="""
    <h1>Hola</h1>
    """
    return HttpResponse(html)
    