from django.contrib import admin
from .models import Itinerary, Accommodation, Destination

# Register your models here.
admin.site.register(Itinerary)
admin.site.register(Accommodation)
admin.site.register(Destination)