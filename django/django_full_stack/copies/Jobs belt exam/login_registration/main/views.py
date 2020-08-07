from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

import bcrypt

from .models import User, Job





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
            'all_jobs': Job.objects.all()
            # 'job_owner': Job.objects.get(id= request.session['userid'])
        }

        return render(request, "dashboard.html", context)


def loggingOut(request):
    request.session.clear()
    return redirect('/')


def jobViewPage(request, id1):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    else:
        context = {
            "viewed_job": Job.objects.get(id= id1)
        }
        return render(request, "jobInfo.html", context)


def createPage(request):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    else:
        return render(request, "createJob.html")

def addingJob(request):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')

    
    else:
        errors = Job.objects.basic_validator_two(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/jobs/new')

        else:
            Job.objects.create(
                title= request.POST['titleLabel'],
                description = request.POST['descriptionLabel'],
                location = request.POST['locationLabel'],
                user_created = User.objects.get(id = request.session['userid'])
            )

            return redirect ('/dashboard')



def removeJob(request, id2):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    else:
        selectedJob = Job.objects.get(id=id2)
        selectedJob.delete()

        return redirect ("/dashboard")


def editPageView(request, id3):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    else:
        context = {
            'all_jobs': Job.objects.all(),
            'selected_job': Job.objects.get(id=id3)
        }
        return render(request, "editPage.html", context)

def editingJob(request, id4):
    if "userid" not in request.session:
        
        messages.error(request, "you are not logged in!!!")
        return redirect('/')
    
    else:
        errors = Job.objects.basic_validator_two(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect(request.META.get('HTTP_REFERER'))

        else:
            selected_job = Job.objects.get(id=id4)

            selected_job.title = request.POST['titleLabel']
            selected_job.description = request.POST['descriptionLabel']
            selected_job.location = request.POST['locationLabel']
            selected_job.user_created = User.objects.get(id = request.session['userid'])

            selected_job.save()

            return redirect('/dashboard')
    
    
    