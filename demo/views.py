import datetime
import random
from django.urls import reverse
from django.core.paginator import Paginator

from django.shortcuts import render
from django.http import HttpResponse

from .models import Car, Person


def demo(request):
    name = request.GET.get("name")
    age = int(request.GET.get("age", 5))
    print(age)
    return HttpResponse(f'hello {name}, {age}')


def cur_time(request):
    return HttpResponse(f"Текущее время: {datetime.datetime.now()}")


def index(request):
    return HttpResponse("<br/>".join([
        f"<h3><a href='{reverse('site88')}'>Главная страница</a></h3>",
        f"<h4><a href='{reverse('cur_time')}'>Текущее время</a></h4>",
        f"<h4><a href='{reverse('temp')}'>Шаблон</a></h4>",
        f"<h4><a href='{reverse('pagi')}'>Paginator</a></h4>",
        f"<h4><a href='{reverse('car')}'>Создание машин</a></h4>",
        f"<h4><a href='{reverse('list_car')}'>Список машин</a></h4>",
        f"<h4><a href='{reverse('create_person')}'>Создание людей</a></h4>",
        f"<h4><a href='{reverse('list_person')}'>Список людей</a></h4>"
    ]))


def summa(request, a, b):
    result = a * b
    return HttpResponse(f"Sum = {result}")


def temp(request):
    context = {
        'test': 5,
        'data': [1, 5, 67],
        'val': 'hello'
    }
    return render(request, 'demo.html', context)


CONTENT = [str(i) for i in range(10000)]


def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)


def new_car(request):
    car = Car(brand=random.choice(['A1', 'A2', 'A3']),
              model=random.choice(['B4', 'B5', 'B6']),
              color=random.choice(['C1', 'C2', 'C3']))
    car.save()
    return HttpResponse(f"Все получилось! Новая машина {car.brand}, {car.model}: {car.color}!")


def list_car(request):
    car_objects = Car.objects.all()
    cars = [f'{i.id}. {i.brand}, {i.model}: {i.color} | {i.owners.count()}' for i in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person.objects.create(name='P', car=car)
    return HttpResponse('Все получилось!')


def list_person(request):
    person_objects = Person.objects.all()
    persons = [f'{person.id}. {person.name}: {person.car}' for person in person_objects]
    return HttpResponse('<br>'.join(persons))