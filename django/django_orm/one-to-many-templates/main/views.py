from django.shortcuts import render, redirect

from .models import User

# Create your views here.
def index_page(request):
    context = {
        "all_users": User.objects.all()
    }

    return render(request, "index.html", context)

def add_user(request):
    created_user = User.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        email=request.POST["email"],
        fav_number=request.POST["fav_number"],
        motto=request.POST["motto"],
    )

    # new_user = User()

    # new_user.save()

    return redirect(f"/users/{created_user.id}")

def view_user(request, user_id):
    context = {
        "this_user": User.objects.get(id=user_id)
    }

    return render(request, "view-user.html", context)