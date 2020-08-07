from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Plant, Comment
import bcrypt


def index(request):
    return render(request, "index.html")


def register_user(request):
    if request.method != "POST":
        return redirect("/")
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_names = request.POST['first_name_input']
        last_names = request.POST['last_name_input']
        emails = request.POST['email_input']
        passwords = request.POST['password_input']
        safe_password = bcrypt.hashpw(
            passwords.encode(), bcrypt.gensalt()).decode()
        new_users = User.objects.create(
            first_name=first_names, last_name=last_names, email=emails, password=safe_password)
        request.session['user'] = new_users.id
        request.session['userName'] = new_users.first_name
    return redirect("/dashboard")


def login_user(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        emails = request.POST['email_input']
        passwords = request.POST['password_input']
        logged_in_user = User.objects.get(email=emails)
        if bcrypt.checkpw(passwords.encode(), logged_in_user.password.encode()):
            request.session['user'] = logged_in_user.id
            request.session['userName'] = logged_in_user.first_name
            return redirect("/dashboard")
        else:
            messages.error(request, 'you canNot login!')
            return redirect("/")


def success(request):
    if 'user' not in request.session:
        return redirect("/")
    # plant_data = Plant.objects.all()
    # context = {
    #     "plants": plant_data
    # }
    return render(request, "dashboard.html")


def logout(request):
    del request.session['user']
    return redirect("/")


def fern_page(request):
    context = {
        'fern_plants': Plant.objects.filter(plant_type="Ferns")
    }
    return render(request, "ferns.html", context)


def succulent_page(request):
    context = {
        'succulent_plants': Plant.objects.filter(plant_type="Succulent")
    }
    return render(request, "succulent.html", context)


def tree_page(request):
    context = {
        'tree_plants': Plant.objects.filter(plant_type="Tree")
    }
    return render(request, "tree.html", context)


def vine_page(request):
    context = {
        'vine_plants': Plant.objects.filter(plant_type="Vine")
    }
    return render(request, "vine.html", context)


def createPlantPageView(request):
    return render(request, "createPlantPage.html")

def createPlantProcessing(request):
    Plant.objects.create(
        plant_type = request.POST['plantTypeLabel'],
        light = request.POST['lightLabel'],
        description = request.POST['descriptionLabel'],
        img = request.POST['imageLabel'],
        user = User.objects.get(id=request.session['user'])

    )

    return redirect('/dashboardAll')

def dashboardAllView(request):
    context = {
        'all_plants': Plant.objects.all()
    }
    return render(request, "dashboardAll.html", context)


def addingComment(request, id):
    Comment.objects.create(
        comment = request.POST['commentLabel'],
        user = User.objects.get(id= request.session['user']),
        plant = Plant.objects.get(id=id)
    )

    return redirect('/fern')


def addingCommentSucculent(request, id2):
    Comment.objects.create(
        comment = request.POST['commentLabel'],
        user = User.objects.get(id= request.session['user']),
        plant = Plant.objects.get(id=id2)
    )

    return redirect('/succulent')

def addingCommentTree(request, id3):
    Comment.objects.create(
        comment = request.POST['commentLabel'],
        user = User.objects.get(id= request.session['user']),
        plant = Plant.objects.get(id=id3)
    )

    return redirect('/tree')

def addingCommentVine(request, id4):
    Comment.objects.create(
        comment = request.POST['commentLabel'],
        user = User.objects.get(id= request.session['user']),
        plant = Plant.objects.get(id=id4)
    )

    return redirect('/vine')