from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pars/', views.pars, name='pars_page'),


]
