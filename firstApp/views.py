from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Hola xd</h1>
    """
    return HttpResponse(html)

def ola(request):
    html="""
    <h1>esta es una lista</h1>
    <li>hola</li>
    <li>ola</li>
    <li>la</li>
    <li>a</li>
    <li></li>
    

    """
    return HttpResponse(html)
