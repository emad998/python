from django.shortcuts import render, HttpResponse, redirect

from .models import User

# Create your views here.
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, "index.html", context)



def create_user(request):
    User.objects.create(
        
        first_name = request.POST["first"],
        last_name = request.POST["last_name"],
        email = request.POST["email"],
        age = request.POST['age']
    )

    return redirect("/")
