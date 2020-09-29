from django.urls import path

from . import views

app_name = "app_django_first"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('index/create/', views.create, name='create'),
    path('index/sp/', views.sp, name='sp'),
    path('index/calc/', views.calc, name='calc'),
    path('template/', views.template, name='template'),
    path('index/form', views.form, name='form'),
    path('index/form2', views.form_name, name='form2'),
    path('index/get', views.form_name, name='form3'),
]
