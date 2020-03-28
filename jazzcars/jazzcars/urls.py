from autos.views import MainView, CategoryView, CarView
from django.urls import path
from django.conf.urls import handler404, handler500
from django.conf import settings


urlpatterns = [
    path('', MainView.as_view()),
    path('category/<str:category>/', CategoryView.as_view()),
    path('car/<int:id>/', CarView.as_view()),
]

handler404 = 'autos.views.view_404'
