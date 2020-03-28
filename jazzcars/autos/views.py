import random

from django.shortcuts import render
from django.views import View

from autos.data import cars

class MainView(View):
    def get(self, request,):
        random.shuffle(cars)
        return render(
            request, 'autos/main.html', context={
                'cars': cars[:6]
            }
        )
class CategoryView(View):
    def get(self, request, category):
        return render(
            request, 'autos/category.html', {'cars': cars, 'pagename': category}
        )

class CarView(View):
    def get(self, request,  id):
        for carr in cars:
            if carr["id"] == id:
                car=carr
                break
        return render(
            request, 'autos/car.html', context={
                'car': car, 'pagename': car['title']
            }
        )

def view_404 (request, exception):
    return render(
        request, '404.html'
    )