from django.shortcuts import render
from .models import *


def view1(request):
    history = History.objects.filter(id__lt=5)
    a = 0
    for i in history:
        a = a + (i.evaluations1)
    schedule = Schedule.objects.filter(id__lt=6)
    return render(request, 'dj1/index.html', {'schedule': schedule, 'history_list': history, 'a': a})


def view2(request):
    history = History.objects.all()
    return render(request, 'dj1/index2.html', {'history_list': history})


def view3(request):
    history = History.objects.all()
    category = Category.objects.all()
    a = 0
    for i in history:
        a = a + (i.evaluations1)
    b = 0
    for i in history:
        b = b + (i.evaluations2)
    return render(request, 'dj1/index3.html', {'category': category, 'history': history, 'a': a, 'b': b})


def view4(request):
    category = Category.objects.all()
    category1 = Category.objects.all().count()
    a = []
    for i in range(category1):
        schedule = Schedule.objects.filter(type2=category[i])
        a.append(schedule)


    return render(request, 'dj1/index4.html', {'schedule_list': schedule, 'category_list': category, 'schedule_list1':a})

# from djLC_app1.models import *
