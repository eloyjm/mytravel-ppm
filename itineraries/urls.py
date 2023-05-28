from django.urls import path
from . import views
from .views import (ItineraryUpdateView, ItineraryDeleteView,)

urlpatterns = [
    path('', views.index, name='index'),
    path('itineraries', views.itineraries, name='itineraries'),
    path('itineraries/<int:id>', views.itineraries_detail, name='itinerary_detail'),
    path('itineraries/<int:pk>/delete', ItineraryDeleteView.as_view(), name="delete_itinerary"),
    path('itineraries/<int:pk>/edit', ItineraryUpdateView.as_view(), name="edit_itinerary"),
    path('destinations', views.destinations, name='destinations'),
    path('destinations/<int:id>', views.destinations_detail, name='destination_detail'),
    path('accommodations', views.accommodations, name='accommodations'),
    path('accommodations/<int:id>', views.accommodations_detail, name='accommodation_detail'),
    path('create_itinerary', views.create_itinerary, name='create_itinerary'),
]