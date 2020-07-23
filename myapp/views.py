from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to index page</h1>")
def home(request):
    return render(request,"myapp/home.html", {"name":"Ashok"})
def fact(request,n):
    n=int(n)
    return HttpResponse("<h4>factorial is {}</h4>".format(factorial(n)))