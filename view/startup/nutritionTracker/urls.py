from django.urls import path
from . import views

urlpatterns = [
    path("/nutFactsResult", views.nutritionFacts),
]