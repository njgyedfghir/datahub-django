# admin_session_timeout.py

from django.contrib import admin

class AdminSessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # Set the session timeout for admin requests (e.g., 1 hour = 3600 seconds)
            request.session.set_expiry(3600)

        response = self.get_response(request)
        return response
