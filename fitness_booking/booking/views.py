from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.filter(datetime__gte=localtime()).order_by('datetime')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_class(request):
    class_id = request.data.get('class_id')
    client_name = request.data.get('client_name')
    client_email = request.data.get('client_email')

    if not all([class_id, client_name, client_email]):
        return Response({'error': 'Missing required fields'}, status=400)

    try:
        fitness_class = FitnessClass.objects.get(id=class_id)
    except FitnessClass.DoesNotExist:
        return Response({'error': 'Class not found'}, status=404)

    if fitness_class.available_slots <= 0:
        return Response({'error': 'No slots available'}, status=400)

    Booking.objects.create(
        fitness_class=fitness_class,
        client_name=client_name,
        client_email=client_email
    )
    fitness_class.available_slots -= 1
    fitness_class.save()

    return Response({'message': 'Booking successful'}, status=201)

@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=400)

    bookings = Booking.objects.filter(client_email=email).order_by('-booked_at')
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
