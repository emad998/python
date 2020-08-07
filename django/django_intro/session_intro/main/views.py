from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if "favorite_color" not in request.session:
        request.session["favorite_color"] = "white"
    
    print(request.session["favorite_color"])
    context = {
        "color": request.session["favorite_color"]
    }
    return render(request, "index.html", context)

def process_form(request):
    # print(request.POST)
    # session is just like a dictionary
    print("hi Emad Hi Emad")
    print(request.POST)
    request.session["favorite_color"] = request.POST['fave_color']

    return redirect("/")