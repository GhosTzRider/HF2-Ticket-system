import logging
from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import User, Category, Service, Priority, Status, Supporter, Ticket, Article, TicketComment

logger = logging.getLogger('TS')
ticket_logger = logging.getLogger('TS.tickets')
article_logger = logging.getLogger('TS.articles')

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

        if ticket.status.name in ('Closed', 'Resolved'):
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
    role = request.session.get('role', 'supporter')
    current_user_id = request.session.get('current_user_id')
    logger.debug("Home view loaded | role=%s user_id=%s", role, current_user_id)

    if role == 'user':
        if current_user_id:
            qs = Ticket.objects.filter(user_id=current_user_id)
        else:
            logger.warning("Home view: user role active but no current_user_id in session")
            qs = Ticket.objects.none()
        context = {
            'total_tickets': qs.count(),
            'open_tickets': qs.filter(status__name='Open').count(),
            'in_progress_tickets': qs.filter(status__name='In Progress').count(),
            'closed_tickets': qs.filter(status__name__in=['Closed', 'Resolved']).count(),
            'recent_tickets': qs.select_related('category', 'priority', 'status').order_by('-created_at')[:10],
            'users': User.objects.all(),
        }
    else:
        context = {
            'total_tickets': Ticket.objects.count(),
            'open_tickets': Ticket.objects.filter(status__name='Open').count(),
            'in_progress_tickets': Ticket.objects.filter(status__name='In Progress').count(),
            'closed_tickets': Ticket.objects.filter(status__name__in=['Closed', 'Resolved']).count(),
            'recent_tickets': Ticket.objects.select_related('category', 'priority', 'status').order_by('-created_at')[:10],
            **calculate_sla(),
        }

    return render(request, 'home.html', context)


def toggle_role(request):
    if request.method == 'POST':
        current = request.session.get('role', 'supporter')
        new_role = 'user' if current == 'supporter' else 'supporter'
        request.session['role'] = new_role
        logger.info("Role toggled: %s -> %s", current, new_role)
    return redirect('home')


def set_current_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            request.session['current_user_id'] = int(user_id)
            logger.info("Active user set to user_id=%s", user_id)
        else:
            logger.warning("set_current_user called with no user_id")
    return redirect('home')

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
        ticket = Ticket.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            user_id=request.POST['user_id'],
            category_id=request.POST['category_id'],
            service_id=request.POST['service_id'],
            priority_id=request.POST['priority_id'],
            status_id=request.POST['status_id'],
        )
        ticket_logger.info(
            "Ticket created | id=%s title=%r user_id=%s priority_id=%s",
            ticket.id, ticket.title, ticket.user_id, ticket.priority_id,
        )
        context['success'] = True

    return render(request, 'create_ticket.html', context)

def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.select_related(
        'user', 'category', 'service', 'priority', 'status', 'supporter'
    ).get(id=ticket_id)
    ticket_logger.debug("Ticket detail viewed | id=%s title=%r", ticket_id, ticket.title)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'assign_supporter':
            supporter_id = request.POST.get('supporter_id')
            ticket.supporter_id = supporter_id
            ticket.save()
            ticket_logger.info(
                "Supporter assigned | ticket_id=%s supporter_id=%s", ticket_id, supporter_id
            )
        elif action == 'change_status':
            status_id = request.POST.get('status_id')
            ticket.status_id = status_id
            ticket.save()
            ticket_logger.info(
                "Status changed | ticket_id=%s new_status_id=%s", ticket_id, status_id
            )
        elif action == 'add_comment':
            TicketComment.objects.create(
                ticket=ticket,
                supporter_id=request.POST.get('comment_supporter_id'),
                user_id=ticket.user_id,
                comment=request.POST.get('comment'),
            )
            ticket_logger.info("Comment added | ticket_id=%s", ticket_id)
        else:
            ticket_logger.warning("Unknown POST action=%r on ticket_id=%s", action, ticket_id)
        return redirect('ticket_detail', ticket_id=ticket_id)

    comments = ticket.comments.select_related('supporter').order_by('created_at')
    context = {
        'ticket': ticket,
        'supporters': Supporter.objects.all(),
        'statuses': Status.objects.all(),
        'comments': comments,
    }
    return render(request, 'ticket_detail.html', context)

def delete_ticket(request, ticket_id):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket_logger.info(
            "Ticket deleted | id=%s title=%r user_id=%s", ticket.id, ticket.title, ticket.user_id
        )
        ticket.delete()
        return redirect('home')
    return redirect('ticket_detail', ticket_id=ticket_id)

def about(request):
    return render(request, 'about.html')

def contact(request):
    context = {
        'supporters': Supporter.objects.all(),
    }
    return render(request, 'contact.html', context)

def tech_knowledge(request):
    query = request.GET.get('q', '').strip()
    articles = Article.objects.select_related('category', 'supporter').order_by('-created_at')
    if query:
        articles = articles.filter(title__icontains=query)
        article_logger.debug("Knowledge base searched | query=%r results=%d", query, articles.count())
    context = {
        'articles': articles,
        'categories': Category.objects.all(),
        'supporters': Supporter.objects.all(),
        'query': query,
    }
    return render(request, 'tech_knowledge.html', context)

def create_article(request):
    if request.method == 'POST':
        article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category_id=request.POST['category_id'],
            supporter_id=request.POST['supporter_id'],
        )
        article_logger.info(
            "Article created | id=%s title=%r supporter_id=%s",
            article.id, article.title, article.supporter_id,
        )
    return redirect('tech_knowledge')

def delete_article(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article_logger.info(
            "Article deleted | id=%s title=%r", article.id, article.title
        )
        article.delete()
    return redirect('tech_knowledge')