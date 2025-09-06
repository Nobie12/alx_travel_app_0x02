from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filterset_fields = {
        'location': ['exact', 'icontains'],
        'available': ['exact'],
        'price_per_night': ['lte', 'gte'],
    }
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price_per_night', 'created_at']
    ordering = ['created_at']
    pagination_class = None  # Add pagination if needed
    permission_classes = []  # Add permissions if needed
    authentication_classes = []  # Add authentication if needed

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_fields = ['user', 'listing', 'check_in', 'check_out']
    search_fields = ['user__username', 'listing__title']
    ordering_fields = ['check_in', 'created_at']
    ordering = ['-created_at']
    pagination_class = None  # Add pagination if needed
    permission_classes = []  # Add permissions if needed
    authentication_classes = []  # Add authentication if needed

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['user', 'listing', 'rating']
    search_fields = ['user__username', 'listing__title', 'comment']
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']
    pagination_class = None  # Add pagination if needed
    permission_classes = []  # Add permissions if needed
    authentication_classes = []  # Add authentication if needed