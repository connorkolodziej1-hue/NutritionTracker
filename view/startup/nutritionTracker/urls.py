from django.urls import path
from . import views

urlpatterns = [
    path("", views.startPage),
    path("nutFactsResult/", views.nutritionFacts),
    path("login/", views.login_user),
    path("logout/", views.logout_user)
]