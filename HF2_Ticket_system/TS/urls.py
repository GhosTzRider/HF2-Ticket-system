from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tech_knowledge/', views.tech_knowledge, name='tech_knowledge'),
    path('ticket/<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
]