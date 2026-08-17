from django.http import HttpResponse
from django.shortcuts import render
from .models import NutritionFacts
import datetime
# Create your views here.
def nutritionFacts(request):
    file = request.POST["file"]
    if request.user.is_authenticated:
        new_facts = NutritionFacts(
            file=file,
            user=request.user,
            timestamp=datetime.datetime.now()
        )
    return HttpResponse("<h1>File received</h1>")

def startPage(request):
    context = {}
    return render(request, "nutritionFactsReader.html", context)