from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def home(request):

    context = {}
    return render (request, "index.html",context)

def contact(request):
    context = {
     
    }

    return render(request, "contact.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)