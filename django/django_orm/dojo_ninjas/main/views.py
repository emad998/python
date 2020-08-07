from django.shortcuts import render, HttpResponse, redirect

from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "all_dojos": Dojo.objects.all()
        
        
    }
    return render(request, "index.html", context)


def addingDojo(request):
    Dojo.objects.create(
        name = request.POST['nameLabel'],
        city = request.POST['cityLabel'],
        state = request.POST['stateLabel']
    )

    return redirect("/")

def addingNinja(request):
    Ninja.objects.create(
        first_name = request.POST['firstName'],
        last_name = request.POST['lastName'],
        dojo = Dojo.objects.get(id=request.POST['dojoName'])  
    )

    return redirect("/")