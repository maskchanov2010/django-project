from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', view1),
    path('2/', view2),
    path('3/', view3),
    path('4/', view4),
]