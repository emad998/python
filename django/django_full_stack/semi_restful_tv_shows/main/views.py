from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages

from .models import Show

# Create your views here.
def allShows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def addingShow(request):
    
    return render(request, 'new.html')

def realAddingShow(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        newShow = Show.objects.create(
        title = request.POST['titleLabel'],
        network = request.POST['networkLabel'],
        release_date = request.POST['releaseDateLabel'],
        description = request.POST['descriptionLabel']
        )

        return redirect(f'/shows/{newShow.id}')



    

def showShow(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }

    return render(request, "show_info.html", context)

def editingShowPage(request, id2):
    current_show = Show.objects.get(id=id2)

    current_show.release_date = current_show.release_date.strftime("%Y-%m-%d")

    context = {
        'this_show': current_show
    }
    return render(request, 'edit_show.html', context)

def updatingShow(request, id3):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        updatedShow = Show.objects.get(id=id3)

        updatedShow.title = request.POST['titleLabel']
        updatedShow.network = request.POST['networkLabel']
        updatedShow.release_date = request.POST['releaseDateLabel']
        updatedShow.description = request.POST['descriptionLabel']

        updatedShow.save()

        return redirect(f"/shows/{updatedShow.id}")


    

def destroyingShow(request, id4):
    show_to_be_destroyed = Show.objects.get(id=id4)
    show_to_be_destroyed.delete()

    return redirect ("/shows")

def index(request):
    return redirect("/shows")