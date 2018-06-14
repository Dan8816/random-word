from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
  # the index function is called when root is visited
def index(request):
    unique_id = get_random_string(length=14)
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    context = {
        'string': unique_id,
        'attempt': request.session['attempt'],
    }
    return render(request, 'randWord_app/index.html', context)

def create(request):
    unique_id = get_random_string(length=14)
    if request.method == "POST":
        request.session['attempt'] +=1   # more on session below
        return redirect("/")
    else:
        return redirect("/")


# Create your views here.
