from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import bcrypt

from .models import User, Product





# Create your views here.
def index(request):
    return render(request, "index.html")

def regUpdate(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['passwordLabel']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        created_user = User.objects.create(
            first_name = request.POST['firstNameLabel'],
            last_name = request.POST['lastNameLabel'],
            email = request.POST['emailLabel'],
            password = pw_hash
        )

        request.session['userid'] = created_user.id
        request.session['userName'] = created_user.first_name
        return redirect('/dashboard')

def loginProcess(request):
    user = User.objects.filter(email=request.POST['emailLabel'])
    if len(user) == 0:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    if bcrypt.checkpw(request.POST['passwordLabel'].encode(), user[0].password.encode()):
        request.session['userid'] = user[0].id
        request.session['userName'] = user[0].first_name
        return redirect("/dashboard")
        
    else:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    


def dashboardView(request):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    else:
        context = {
            'all_products': Product.objects.all()
        }
        return render(request, "dashboard.html", context)


def loggingOut(request):
    request.session.clear()
    return redirect('/')


def createProductPageView(request):
    return render(request, "createProduct.html")

def createProductProcessing(request):
    Product.objects.create(
        name=request.POST['nameLabel'],
        inventory=request.POST['inventoryLabel'],
        quantity_sold=request.POST['quantitySoldLabel'],
        desc=request.POST['descLabel'],
        image=request.POST['imageLabel'],
        user= User.objects.get(id=request.session['userid']),
        price = request.POST['priceLabel']

    )

    return redirect('/dashboard')