import time
from collections import defaultdict
from threading import Lock

from django.http import HttpResponse


class TicketRateLimitMiddleware:
    """
    Limits ticket creation to RATE POSTs per WINDOW seconds per IP address.
    No external dependencies — uses an in-memory sliding window counter.

    Default: 10 ticket submissions per 60 seconds per IP.
    Adjust RATE and WINDOW below to tune the limits.
    """

    RATE   = 10   # max POST submissions allowed
    WINDOW = 60   # rolling window in seconds

    _buckets: dict = defaultdict(list)
    _lock: Lock    = Lock()

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.path == '/create/':
            ip  = self._get_client_ip(request)
            now = time.monotonic()

            with self._lock:
                # Drop timestamps that have fallen outside the window
                self._buckets[ip] = [
                    t for t in self._buckets[ip] if now - t < self.WINDOW
                ]

                if len(self._buckets[ip]) >= self.RATE:
                    return HttpResponse(
                        f"Too many ticket submissions. "
                        f"You may submit at most {self.RATE} tickets per {self.WINDOW} seconds. "
                        f"Please wait before trying again.",
                        status=429,
                        content_type='text/plain',
                    )

                self._buckets[ip].append(now)

        return self.get_response(request)

    @staticmethod
    def _get_client_ip(request) -> str:
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            return forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR', 'unknown')
