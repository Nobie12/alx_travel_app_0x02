from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_titles = [
            "Cozy Cottage", "Modern Apartment", "Beach House", "Mountain Cabin", "City Studio"
        ]
        sample_descriptions = [
            "A lovely place to relax.", "Close to all amenities.", "Perfect for weekend getaways.",
            "Stunning views included.", "Ideal for families."
        ]
        sample_locations = [
            "Nairobi", "Mombasa", "Kisumu", "Naivasha", "Nakuru"
        ]

        for i in range(10):  # create 10 sample listings
            listing = Listing.objects.create(
                title=random.choice(sample_titles) + f" #{i+1}",
                description=random.choice(sample_descriptions),
                price_per_night=round(random.uniform(50, 300), 2),
                location=random.choice(sample_locations),
                available=random.choice([True, False])
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))
