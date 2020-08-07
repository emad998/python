from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    request.session['count'] = 0
    return render(request, "index.html")

def word(request):
    request.session['rand'] = get_random_string(length=14)
    request.session['count'] +=1
    return HttpResponse(f"Random Word attempt {request.session['count']} and random string {request.session['rand']}")

def reset(request):
    
    request.session.clear()

    return redirect('/')