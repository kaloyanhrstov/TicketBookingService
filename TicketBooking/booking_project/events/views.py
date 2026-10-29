from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Event, Booking
from .serializers import (
    EventSerializer,
    BookingSerializer,
    BookingCreateSerializer,
    RegisterSerializer
)
from rest_framework import generics, permissions
from .permissions import IsAdminOrReadOnly
from django.contrib.auth import login
from .serializers import RegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Event.objects.all().order_by("-starts_at")
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user.id)


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all().order_by("-created_at")
        return Booking.objects.filter(user_id=user.id).order_by("-created_at")

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return BookingCreateSerializer
        return BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)