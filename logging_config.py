"""
HF2 Ticket System - Logging Configuration
==========================================
Central logging configuration for the HF2 Ticket System Django project.

Log files are written to the 'logs/' directory next to this file:
  - app.log     : General application activity (INFO+)
  - error.log   : Errors and critical issues only (ERROR+)
  - tickets.log : Ticket-specific operations (DEBUG+)

Usage in any Python module:
    import logging
    logger = logging.getLogger('TS')          # app-level logger
    logger = logging.getLogger('TS.tickets')  # ticket-specific logger
    logger = logging.getLogger('TS.articles') # article-specific logger
"""

import logging
import logging.handlers
from pathlib import Path

# Resolve the logs directory relative to this file
LOGS_DIR = Path(__file__).resolve().parent / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

# ─── Formatters ──────────────────────────────────────────────────────────────

DETAILED_FORMAT = (
    '[%(asctime)s] %(levelname)-8s %(name)s:%(lineno)d | %(message)s'
)
SIMPLE_FORMAT = '[%(asctime)s] %(levelname)-8s | %(message)s'

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# ─── Configuration Dictionary ────────────────────────────────────────────────

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'detailed': {
            'format': DETAILED_FORMAT,
            'datefmt': DATE_FORMAT,
        },
        'simple': {
            'format': SIMPLE_FORMAT,
            'datefmt': DATE_FORMAT,
        },
    },

    'handlers': {
        # Console output (INFO and above)
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
        },

        # General application log — rotates at 10 MB, keeps 14 backups
        'app_file': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': str(LOGS_DIR / 'app.log'),
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 14,
            'encoding': 'utf-8',
            'level': 'INFO',
            'formatter': 'detailed',
        },

        # Error log — only ERROR and CRITICAL, rotates at 10 MB, keeps 30 backups
        'error_file': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': str(LOGS_DIR / 'error.log'),
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 30,
            'encoding': 'utf-8',
            'level': 'ERROR',
            'formatter': 'detailed',
        },

        # Ticket operations log — DEBUG and above, rotates at 10 MB, keeps 7 backups
        'tickets_file': {
            'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
            'filename': str(LOGS_DIR / 'tickets.log'),
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 7,
            'encoding': 'utf-8',
            'level': 'DEBUG',
            'formatter': 'detailed',
        },
    },

    'loggers': {
        # Django framework logger
        'django': {
            'handlers': ['console', 'app_file', 'error_file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django request logger (logs 4xx/5xx)
        'django.request': {
            'handlers': ['error_file', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
        # Django database queries (set to WARNING in prod to avoid noise)
        'django.db.backends': {
            'handlers': ['app_file'],
            'level': 'WARNING',
            'propagate': False,
        },

        # TS app — root logger for the whole Ticket System app
        'TS': {
            'handlers': ['console', 'app_file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # TS sub-loggers for specific domains
        'TS.tickets': {
            'handlers': ['tickets_file', 'console', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'TS.articles': {
            'handlers': ['tickets_file', 'console', 'error_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },

    # Root fallback logger
    'root': {
        'handlers': ['console', 'error_file'],
        'level': 'WARNING',
    },
}
