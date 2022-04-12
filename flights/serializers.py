from dataclasses import fields
from rest_framework import serializers
from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            "id",
            "destination",
            "time",
            "price"
        ]
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            "flight",
            "date"
        ]