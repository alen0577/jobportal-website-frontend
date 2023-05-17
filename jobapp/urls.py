from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginhome,name='loginhome'),
    path('home/',views.index,name='index')
]