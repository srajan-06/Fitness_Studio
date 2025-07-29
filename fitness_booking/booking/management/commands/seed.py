from django.core.management.base import BaseCommand
from booking.models import FitnessClass
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed the database with sample classes'

    def handle(self, *args, **kwargs):
        FitnessClass.objects.all().delete()
        now = timezone.now()
        classes = [
            {'name': 'Yoga', 'datetime': now + timedelta(days=1), 'instructor': 'Alice', 'total_slots': 10},
            {'name': 'Zumba', 'datetime': now + timedelta(days=2), 'instructor': 'Bob', 'total_slots': 15},
            {'name': 'HIIT', 'datetime': now + timedelta(days=3), 'instructor': 'Charlie', 'total_slots': 12},
        ]
        for c in classes:
            FitnessClass.objects.create(
                name=c['name'],
                datetime=c['datetime'],
                instructor=c['instructor'],
                total_slots=c['total_slots'],
                available_slots=c['total_slots']
            )
        self.stdout.write(self.style.SUCCESS('Sample classes seeded'))
