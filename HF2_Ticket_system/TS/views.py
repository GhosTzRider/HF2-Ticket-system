from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User, Category, Service, Priority, Status, Supporter, Ticket

SLA_THRESHOLDS = {
    'critical': timedelta(hours=4),
    'high':     timedelta(hours=8),
    'medium':   timedelta(hours=24),
    'low':      timedelta(hours=72),
}

def calculate_sla():
    tickets = Ticket.objects.select_related('priority', 'status').all()
    met = 0
    breached = 0
    now = timezone.now()

    for ticket in tickets:
        threshold = SLA_THRESHOLDS.get(ticket.priority.name.lower())
        if not threshold:
            continue

        if ticket.status.name == 'Closed':
            elapsed = ticket.updated_at - ticket.created_at
        else:
            elapsed = now - ticket.created_at

        if elapsed <= threshold:
            met += 1
        else:
            breached += 1

    total = met + breached
    return {
        'sla_met':          met,
        'sla_breached':     breached,
        'sla_total':        total,
        'sla_met_pct':      round((met / total) * 100) if total else 0,
        'sla_breached_pct': round((breached / total) * 100) if total else 0,
    }

# Create your views here.

def home(request):
    context = {
        'total_tickets': Ticket.objects.count(),
        'open_tickets': Ticket.objects.filter(status__name='Open').count(),
        'in_progress_tickets': Ticket.objects.filter(status__name='In Progress').count(),
        'closed_tickets': Ticket.objects.filter(status__name='Closed').count(),
        'recent_tickets': Ticket.objects.select_related('category', 'priority', 'status').order_by('-created_at')[:10],
        **calculate_sla(),
    }
    return render(request, 'home.html', context)

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

def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.select_related(
        'user', 'category', 'service', 'priority', 'status', 'supporter'
    ).get(id=ticket_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'assign_supporter':
            ticket.supporter_id = request.POST.get('supporter_id')
        elif action == 'change_status':
            ticket.status_id = request.POST.get('status_id')
        ticket.save()
        return redirect('ticket_detail', ticket_id=ticket_id)

    context = {
        'ticket': ticket,
        'supporters': Supporter.objects.all(),
        'statuses': Status.objects.all(),
    }
    return render(request, 'ticket_detail.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tech_knowledge(request):
    return render(request, 'tech_knowledge.html')