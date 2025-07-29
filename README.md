# Fitness_Studio
Omnify Python Developer Assignment

# Fitness Booking API

A simple Django REST API for booking fitness classes.

## Endpoints

- `GET /classes` - List of available classes
- `POST /book` - Book a class
- `GET /bookings?email=...` - View bookings by email

## Setup

```bash
git clone ...
cd fitness_booking
pip install -r requirements.txt
python manage.py migrate
python manage.py seed  # Load sample classes
python manage.py runserver
