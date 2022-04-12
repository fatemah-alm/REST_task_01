from .models import Flight, Booking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FlightSerializer, BookingSerializer
from datetime import date



@api_view(['GET'])
def flights(request, *args, **kwargs):
    
    flight_data = Flight.objects.all()
    res = []
    for instance in flight_data:
        data = FlightSerializer(instance).data
        res.append(data)
    return Response(res)


@api_view(['GET'])
def bookings(request, *args, **kwargs):
    booking_data = Booking.objects.filter(date__gt=date.today())
    res = []
    for instance in booking_data:
        data = BookingSerializer(instance).data
        res.append(data)
    return Response(res)


