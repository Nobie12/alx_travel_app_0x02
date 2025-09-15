from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

class Listing(models.Model):
    """Represents a travel listing."""
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=225)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Represents a booking for a listing by a user."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booking for {self.listing.title}"


class Review(models.Model):
    """User review for a listing."""
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} by {self.user.username} on {self.listing.title}"

class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = "P", "Pending"
        SUCCESS = "S", "success"
        FAILED = "F", "failed"
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    payment_status = models.CharField(max_length=200, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    amount = models.IntegerField()
    transaction_id = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Foreign key
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.booking} - {self.payment_status} - {self.amount}"