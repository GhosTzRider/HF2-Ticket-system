from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Category, Service, Priority, Status, Supporter, Ticket

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create_ticket(request):
    open_status = Status.objects.filter(name='Open').first()

    context = {
        'users': User.objects.all(),
        'categories': Category.objects.all(),
        'services': Service.objects.all(),
        'priorities': Priority.objects.all(),
        'open_status_id': open_status.id if open_status else '',
    }

    if request.method == 'POST':
        Ticket.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            user_id=request.POST['user_id'],
            category_id=request.POST['category_id'],
            service_id=request.POST['service_id'],
            priority_id=request.POST['priority_id'],
            status_id=request.POST['status_id'],
        )
        context['success'] = True

    return render(request, 'create_ticket.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tech_knowledge(request):
    return render(request, 'tech_knowledge.html')