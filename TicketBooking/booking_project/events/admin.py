from django.contrib import admin
from .models import Event, Booking


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "starts_at", "ends_at", "capacity")
    search_fields = ("title",)
    list_filter = ("starts_at", "ends_at")


class BookingAdmin(admin.ModelAdmin):
    list_display = ("event", "user_id", "quantity", "status")
    search_fields = ("event__title", "user_id")
    list_filter = ("status",)


admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
