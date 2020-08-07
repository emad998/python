from django.shortcuts import render, HttpResponse

# Create your views here.
def index_func(request):
    # return HttpResponse("<h1>Hello from Django</h1>")
    context = {
        "first_name": "Morley",
        "users": [
            "Jason Brady",
            "Raymond Smith",
            "Yuri Chalmers"
        ]
    }

    return render(request, "index.html", context)