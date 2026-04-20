from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_ticket(request):
    return render(request, 'create_ticket.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tech_knowledge(request):
    return render(request, 'tech_knowledge.html')