from django.db import models
from django.db.models import Q, F


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(TimeStampedModel):
    owner_id = models.PositiveBigIntegerField(db_index=True)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)

    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()

    capacity = models.PositiveIntegerField()
    ticket_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(ends_at__gt=F("starts_at")),
                name="event_end_after_start",
            ),
        ]

    def __str__(self):
        return self.title


class Booking(TimeStampedModel):
    class Status(models.TextChoices):
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    user_id = models.PositiveBigIntegerField(db_index=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.CONFIRMED,
    )

    class Meta:
        indexes = [
            models.Index(fields=["event", "status"]),
            models.Index(fields=["user_id", "status"]),
        ]

    def __str__(self):
        return f"Booking #{self.pk} - Event #{self.event_id}"