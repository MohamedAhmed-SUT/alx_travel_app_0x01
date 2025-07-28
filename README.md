# ALX Travel App - Milestone 3: API Development

This project milestone focuses on building the core API endpoints for the Listings and Bookings functionalities using Django REST Framework.

## Key Components

-   **`listings/views.py`**: Contains `ModelViewSet` classes for the `Listing` and `Booking` models. These viewsets provide full CRUD (Create, Read, Update, Delete) functionality.
-   **`listings/urls.py`**: Configures a `DefaultRouter` to automatically generate the RESTful API URL patterns for the viewsets.
-   **API Endpoints**: The following endpoints are now available under the `/api/` prefix:
    -   `/api/listings/`
    -   `/api/bookings/`

## How to Test

1.  Run the development server: `python manage.py runserver`.
2.  Use a tool like Postman to send `GET`, `POST`, `PUT`, and `DELETE` requests to the endpoints listed above to test the CRUD operations.