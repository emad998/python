from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    request.session['gold'] = 0
    request.session['p'] = []
    return render(request, 'index.html')

def gold_processing(request):
    if request.POST['farm'] == "farm":
        rand = random.randint(10,20)
        request.session['gold'] += rand
        
    elif request.POST['farm'] == "cave":
        rand = random.randint(5,10)
        request.session['gold'] += rand
    elif request.POST['farm'] == "house":
        rand = random.randint(2,5)
        request.session['gold'] += rand
    elif request.POST['farm'] == "casino":
        rand = random.randint(-50,50)
        request.session['gold'] += rand

    if rand >= 0:
        request.session['p'].append("you earned " + str(rand) + " gold from the " + request.POST['farm'])
    elif rand <= 0:
        request.session['p'].append("entered a casino and lost" + str(rand) + " golds ... ouch")
    
    

    return render(request, 'index.html')


def reset(request):
    
    request.session.clear()

    return redirect('/')