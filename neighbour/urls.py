from django.urls import path
from . import views

urlpatherns= {
    path('', views.index, name= 'index'),

}