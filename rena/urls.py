from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('done/<main>', done, name="done"),
    path('delete/<main>', delete, name="delete"),
    path('undone/<main>', undone, name="undone"),
    path('stude', stude, name="student"),
    path('remove/<main>', remove, name="remove"),
    path('calculator', calculator, name="calculator"),
    path('result', result, name="result"),
    path('submit', submit, name="submit"),
    path('signin', signin, name="signin"),
    path('signout', signout, name="signout"),
    path('person', person, name="person"),
]
