from autos.views import MainView, CategoryView, CarView
from django.urls import path
  
urlpatterns = [
    path('', MainView.as_view()),
    path('category/<str:category>/', CategoryView.as_view()),
    path('car/<int:id>/', CarView.as_view()),
]
