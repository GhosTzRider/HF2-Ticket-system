from django.db import connections
from django.test.runner import DiscoverRunner

from TS.models import (
    Article, Category, Priority, Service,
    Status, Supporter, Ticket, TicketComment, User,
)

# Dependency order: tables with no FKs first
MODELS_IN_ORDER = [
    User, Supporter, Category, Service, Priority, Status,
    Ticket, TicketComment, Article,
]


class UnmanagedModelsTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        result = super().setup_databases(**kwargs)
        connection = connections['default']
        with connection.schema_editor() as editor:
            for model in MODELS_IN_ORDER:
                editor.create_model(model)
        return result
