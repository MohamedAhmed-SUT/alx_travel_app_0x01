from rest_framework import viewsets, permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows property listings to be viewed or edited.
    Provides full CRUD functionality.
    """
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    # Allow any user to view listings, but only authenticated users to create/edit.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Associate the listing with the user who created it.
        """
        serializer.save(host=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or created.
    """
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only see their own bookings.
        An admin should be able to see all bookings.
        """
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Booking.objects.all()
        return Booking.objects.filter(guest=user)

    def perform_create(self, serializer):
        """
        Associate the booking with the user who created it (the guest).
        Also, calculate the total price before saving.
        """
        listing = serializer.validated_data['listing']
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        
        # Calculate number of nights
        num_nights = (end_date - start_date).days
        if num_nights <= 0:
            from rest_framework.exceptions import ValidationError
            raise ValidationError("End date must be after start date.")
            
        total_price = listing.price_per_night * num_nights

        serializer.save(guest=self.request.user, total_price=total_price)