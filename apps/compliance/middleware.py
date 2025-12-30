from .models import AuditLog

class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            AuditLog.objects.create(
                user=request.user,
                action=request.method,
                model=request.path,
                object_id='N/A',
                ip_address=request.META.get('REMOTE_ADDR')
            )

        return response
