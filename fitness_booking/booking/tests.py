from django.test import TestCase
from .models import FitnessClass, Booking
from django.utils import timezone
from datetime import timedelta

class BookingTest(TestCase):
    def setUp(self):
        self.cls = FitnessClass.objects.create(
            name="Yoga", datetime=timezone.now() + timedelta(days=1),
            instructor="Test", total_slots=5, available_slots=5
        )

    def test_booking_success(self):
        Booking.objects.create(
            fitness_class=self.cls,
            client_name="Test User",
            client_email="test@example.com"
        )
        self.cls.refresh_from_db()
        self.assertEqual(self.cls.available_slots, 4)
