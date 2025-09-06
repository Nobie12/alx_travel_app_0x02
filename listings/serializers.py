from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all(), source='listing', write_only=True)

    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['id', 'listing', 'user', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):

    listing = ListingSerializer(read_only=True)
    listing_id = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all(), source='listing', write_only=True)

    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'listing', 'user', 'created_at']