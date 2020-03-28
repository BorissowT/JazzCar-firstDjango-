from django.shortcuts import render
from django.views import View

from autos.data import cars

class MainView(View):
    def get(self, request,):
        return render(
            request, 'autos/main.html', context={
                'cars': cars
            }
        )
class CategoryView(View):
    def get(self, request, category):
        return render(
            request, 'autos/category.html', context={
                'cars': cars, 'pagename': category
            }
        )

class CarView(View):
    def get(self, request,  id, *args, **kwargs):
        for carr in cars:
            if carr["id"] == id:
                car=carr
                break
        return render(
            request, 'autos/car.html', context={
                'car': car, 'pagename': car['title']
            }
        )