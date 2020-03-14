
from django.contrib import admin
from django.urls import path
from autos.views import MainView

urlpatterns = [
    path('', MainView.as_view()),
]
