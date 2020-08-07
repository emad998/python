from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index_func(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "index.html", context)