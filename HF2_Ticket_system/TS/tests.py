from django.test import TestCase

from TS.models import (
    Category, Priority, Service,
    Status, Supporter, Ticket, TicketComment, User,
)


class ModelStrTestCase(TestCase):
    def test_user_str(self):
        user = User(first_name='John', last_name='Doe', email='john@example.com')
        self.assertEqual(str(user), 'John Doe')

    def test_supporter_str(self):
        supporter = Supporter(first_name='Jane', last_name='Smith', email='jane@example.com')
        self.assertEqual(str(supporter), 'Jane Smith')

    def test_category_str(self):
        self.assertEqual(str(Category(name='Software')), 'Software')

    def test_priority_str(self):
        self.assertEqual(str(Priority(name='High')), 'High')

    def test_status_str(self):
        self.assertEqual(str(Status(name='Open')), 'Open')

    def test_ticket_str(self):
        self.assertEqual(str(Ticket(title='Test Ticket')), 'Test Ticket')


class TicketCreationTestCase(TestCase):
    def test_ticket_creation(self):
        user = User.objects.create(first_name='Test', last_name='User', email='test@example.com')
        supporter = Supporter.objects.create(first_name='Support', last_name='Staff', email='support@example.com')
        category = Category.objects.create(name='Software')
        service = Service.objects.create(name='IT Support')
        priority = Priority.objects.create(name='High')
        status = Status.objects.create(name='Open')

        ticket = Ticket.objects.create(
            title='Test Ticket',
            description='This is a test ticket.',
            user=user,
            category=category,
            service=service,
            priority=priority,
            status=status,
            supporter=supporter,
        )

        self.assertEqual(ticket.title, 'Test Ticket')
        self.assertEqual(ticket.description, 'This is a test ticket.')
        self.assertEqual(ticket.user.first_name, 'Test')
        self.assertEqual(ticket.category.name, 'Software')
        self.assertEqual(ticket.service.name, 'IT Support')
        self.assertEqual(ticket.priority.name, 'High')
        self.assertEqual(ticket.status.name, 'Open')
        self.assertEqual(ticket.supporter.first_name, 'Support')

    def test_ticket_comment_creation(self):
        user = User.objects.create(first_name='Test', last_name='User', email='test2@example.com')
        supporter = Supporter.objects.create(first_name='Support', last_name='Staff', email='support2@example.com')
        category = Category.objects.create(name='Hardware')
        service = Service.objects.create(name='Help Desk')
        priority = Priority.objects.create(name='Low')
        status = Status.objects.create(name='Open')

        ticket = Ticket.objects.create(
            title='Comment Test Ticket',
            description='Ticket for comment test.',
            user=user,
            category=category,
            service=service,
            priority=priority,
            status=status,
        )

        comment = TicketComment.objects.create(
            ticket=ticket,
            user=user,
            supporter=supporter,
            comment='This is a test comment.',
        )

        self.assertEqual(comment.comment, 'This is a test comment.')
        self.assertEqual(comment.ticket.title, 'Comment Test Ticket')
        self.assertEqual(ticket.comments.count(), 1)
