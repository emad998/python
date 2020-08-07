from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index_func(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")


def show(request, my_num):
    
    return HttpResponse("placeholder to display blog number " + str(my_num))


def edit(request, edit_num):
    return HttpResponse(f"placeholder to edit blog {edit_num}")


def destroy(request):
    return redirect("/")