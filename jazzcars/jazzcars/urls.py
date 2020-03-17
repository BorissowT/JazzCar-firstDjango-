from django.contrib import admin
from django.urls import path
from autos.views import MainView, CategoryView, CarView

urlpatterns = [
    path('', MainView.as_view()),
    path('<str:category>/', CategoryView.as_view()),
    path('category/<int:id>', CarView.as_view()),
]
