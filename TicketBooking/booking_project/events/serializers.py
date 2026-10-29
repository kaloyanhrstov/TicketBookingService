from rest_framework import serializers
from .models import Event, Booking
from django.db.models import Sum


from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EventSerializer(serializers.ModelSerializer):
    # available_tickets = serializers.SerializerMethodField()
    booked_tickets = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'


    # def get_available_tickets(self, event):
    #     booked = event.bookings.filter(
    #         status=Booking.Status.CONFIRMED
    #     ).aggregate(total=Sum("quantity"))["total"] or 0

    #     return event.capacity - booked

    def get_booked_tickets(self, event):
        return event.bookings.filter(
            status=Booking.Status.CONFIRMED
        ).aggregate(total=Sum("quantity"))["total"] or 0


class BookingCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(min_value=1, read_only=True)
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Booking
        fields = ['event', 'user_id', 'quantity']

class BookingSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(
            source="event.title",
            read_only=True,
        )

    class Meta:
        model = Booking
        fields = '__all__'

