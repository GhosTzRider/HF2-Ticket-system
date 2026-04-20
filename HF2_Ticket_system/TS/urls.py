from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tech_knowledge/', views.tech_knowledge, name='tech_knowledge'),
]