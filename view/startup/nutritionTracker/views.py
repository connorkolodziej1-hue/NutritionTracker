from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import NutritionFacts
from django.contrib.auth.models import User
import datetime
# Create your views here.
def nutritionFacts(request):
    if request.method == "POST":
        file = request.POST["file"]
        if request.user.is_authenticated:
            new_facts = NutritionFacts(
                file=file,
                user=request.user,
                timestamp=datetime.datetime.now()
            )
        return HttpResponse("<h1>File received</h1>")
    
    return HttpResponse("<h1>INVALID REQUEST</h1>")
    

def startPage(request):
    context = {}
    return render(request, "nutritionFactsReader.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/nutritionTracker/")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("/nutritionTracker/")


    return redirect("/nutritionTracker/")

def logout_user(request):
    logout(request)
    return redirect("/nutritionTracker/")
    

