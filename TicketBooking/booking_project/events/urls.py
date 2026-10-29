from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, BookingViewSet, RegisterView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/auth/register/', RegisterView.as_view(), name='api-register'),
    path('api-auth/', include('rest_framework.urls')),
]