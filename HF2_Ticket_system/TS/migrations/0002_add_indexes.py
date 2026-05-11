from django.db import migrations


_CREATE = [
    """
    IF NOT EXISTS (
        SELECT 1 FROM sys.indexes
        WHERE name = 'idx_tickets_user_id'
          AND object_id = OBJECT_ID('tickets')
    )
    CREATE INDEX idx_tickets_user_id ON tickets (user_id);
    """,
    """
    IF NOT EXISTS (
        SELECT 1 FROM sys.indexes
        WHERE name = 'idx_tickets_status_id'
          AND object_id = OBJECT_ID('tickets')
    )
    CREATE INDEX idx_tickets_status_id ON tickets (status_id);
    """,
    """
    IF NOT EXISTS (
        SELECT 1 FROM sys.indexes
        WHERE name = 'idx_tickets_priority_id'
          AND object_id = OBJECT_ID('tickets')
    )
    CREATE INDEX idx_tickets_priority_id ON tickets (priority_id);
    """,
    """
    IF NOT EXISTS (
        SELECT 1 FROM sys.indexes
        WHERE name = 'idx_tickets_supporter_id'
          AND object_id = OBJECT_ID('tickets')
    )
    CREATE INDEX idx_tickets_supporter_id ON tickets (supporter_id);
    """,
    """
    IF NOT EXISTS (
        SELECT 1 FROM sys.indexes
        WHERE name = 'idx_tickets_created_at'
          AND object_id = OBJECT_ID('tickets')
    )
    CREATE INDEX idx_tickets_created_at ON tickets (created_at DESC);
    """,
    """
    IF NOT EXISTS (
        SELECT 1 FROM sys.indexes
        WHERE name = 'idx_statuses_name'
          AND object_id = OBJECT_ID('statuses')
    )
    CREATE INDEX idx_statuses_name ON statuses (name);
    """,
]

_DROP = [
    "IF EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'idx_tickets_user_id'     AND object_id = OBJECT_ID('tickets'))  DROP INDEX idx_tickets_user_id     ON tickets;",
    "IF EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'idx_tickets_status_id'   AND object_id = OBJECT_ID('tickets'))  DROP INDEX idx_tickets_status_id   ON tickets;",
    "IF EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'idx_tickets_priority_id' AND object_id = OBJECT_ID('tickets'))  DROP INDEX idx_tickets_priority_id ON tickets;",
    "IF EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'idx_tickets_supporter_id'AND object_id = OBJECT_ID('tickets'))  DROP INDEX idx_tickets_supporter_id ON tickets;",
    "IF EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'idx_tickets_created_at'  AND object_id = OBJECT_ID('tickets'))  DROP INDEX idx_tickets_created_at  ON tickets;",
    "IF EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'idx_statuses_name'       AND object_id = OBJECT_ID('statuses')) DROP INDEX idx_statuses_name       ON statuses;",
]


class Migration(migrations.Migration):

    dependencies = [
        ('TS', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(sql=_CREATE, reverse_sql=_DROP),
    ]
