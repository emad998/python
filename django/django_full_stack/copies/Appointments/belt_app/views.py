
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Appointment
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
        request.session['user_name'] = new_users.first_name
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
            request.session['user_name'] = logged_in_user.first_name
            request.session['user'] = logged_in_user.id
            return redirect("/dashboard")
        else:
            messages.error(request, 'you canNot login!')
            return redirect("/")


def success(request):
    if 'user' not in request.session:
        return redirect("/")
    appointment_data = Appointment.objects.all()
    context = {
        "appointments": appointment_data
    }
    return render(request, "dashboard.html", context)


def logout(request):
    del request.session['user']
    return redirect("/")


def create_appointment(request):
    errors = Appointment.objects.appointment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            # redirects to same page youre on
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        user = User.objects.get(id=request.session["user"])
        Appointment.objects.create(
            user=user, tasks=request.POST['task'], date=request.POST["date"], status=request.POST["status"])
        return redirect("/dashboard")


def edit(request, Val):
    context = {
        "selected_appointment": Appointment.objects.get(id=Val)
    }
    return render(request, "edit.html", context)


def edit_appointment(request, Val):
    errors = Appointment.objects.appointment_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            # redirects to same page youre on
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        this_appointment = Appointment.objects.get(id=Val)
        this_appointment.task = request.POST['task']
        this_appointment.date = request.POST["date"]
        this_appointment.status = request.POST['status']
        this_appointment.save()
        return redirect("/dashboard")


def remove_appointment(request, Val):
    appointment = Appointment.objects.get(id=Val)
    appointment.delete()
    return redirect("/dashboard")


def addAppointment(request):
    return render(request, "create_appointment.html")


def view_appointment(request, x):
    appointments_id = Appointment.objects.get(id=x)
    context = {
        "appointments": appointments_id
    }
    return render(request, "view.html", context)
