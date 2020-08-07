from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import bcrypt

from .models import User, Message, Comment





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
        User.objects.create(
            first_name = request.POST['firstNameLabel'],
            last_name = request.POST['lastNameLabel'],
            email = request.POST['emailLabel'],
            password = pw_hash
        )
        return redirect('/')

def loginProcess(request):
    user = User.objects.filter(email=request.POST['emailLabel'])
    if len(user) == 0:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    if bcrypt.checkpw(request.POST['passwordLabel'].encode(), user[0].password.encode()):
        request.session['userid'] = user[0].id
        request.session['userName'] = user[0].first_name

        return redirect("/success")
    
        
    else:
        messages.error(request, "Please check your email and password")
        return redirect("/")
    




def successView(request):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    else:
        context = {
            "all_messages": Message.objects.all().order_by('-created_at'),
            "all_comments": Comment.objects.all().order_by('-created_at'),
        }
        return render(request, "success.html", context)


def loggingOut(request):
    request.session.clear()
    return redirect('/')


def addingMessage(request):
    Message.objects.create(
        message = request.POST['messageLabel'],
        user = User.objects.get(id = request.session['userid'])
    )
    return redirect("/success")


def addingComment(request, id1):
    Comment.objects.create(
        comment = request.POST['commentLabel'],
        user = User.objects.get(id = request.session['userid']),
        message = Message.objects.get(id=id1)

    )

    return redirect('/success')
