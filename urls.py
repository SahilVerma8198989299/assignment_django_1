from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path("", views.index, name='myapp'),
    path("self", views.self, name="self"),
    path("nam", views.name, name="nam"),
    path("contact", views.contact, name="contact"),
    path("", views.verma, name="verma"),
    path("save", views.save, name="save")
]