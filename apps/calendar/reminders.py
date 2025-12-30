from django.utils.timezone import now
from datetime import timedelta
from .models import CourtEvent

def upcoming_deadlines(hours=24):
    deadline = now() + timedelta(hours=hours)
    return CourtEvent.objects.filter(start__lte=deadline)
