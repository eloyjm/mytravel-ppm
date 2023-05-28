from django.shortcuts import render
from .models import Itinerary, Accommodation, Destination
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItineraryForm
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    title = "Welcome to MYTRAVEL"
    return render(request, 'index.html', {
        'title':title
    })

@login_required
def itineraries(request):
    itineraries = Itinerary.objects.filter(user=request.user)
    return render(request, 'itineraries/itineraries.html', {
        'itineraries': itineraries
    })

def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destinations.html', {
        'destinations':destinations
    })

def accommodations(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'accommodations/accommodations.html', {
        'accommodations':accommodations
    })

@login_required
def itineraries_detail(request, id):
    itinerary = get_object_or_404(Itinerary, id=id)
    destinations=itinerary.destinations.all()
    accommodations=itinerary.accommodations.all()

    return render(request, 'itineraries/detail.html', {
        'itinerary': itinerary, 'destinations':destinations, 'accommodations':accommodations
    })

def destinations_detail(request, id):
    destination = get_object_or_404(Destination, id=id)
    accommodations = Accommodation.objects.filter(destination_id=id).all()
    return render(request, 'destinations/detail.html', {
        'destination': destination, 'accommodations':accommodations
    })

def accommodations_detail(request, id):
    accommodation = get_object_or_404(Accommodation, id=id)
    return render(request, 'accommodations/detail.html', {
        'accommodation': accommodation,
    })

@login_required
def create_itinerary(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            form_clean=form.cleaned_data
            nuevo_it=Itinerary.objects.create(
                name=form_clean['name'],
                description=form_clean['description'],
                startDate=form_clean['startDate'],
                finishDate=form_clean['finishDate'],
                user = request.user
            )
            nuevo_it.destinations.set(form_clean['destinations'])
            nuevo_it.accommodations.set(form_clean['accommodations'])
            return redirect('itineraries')

    else:
        form = ItineraryForm()
    return render(request, 'itineraries/create_itinerary.html', {'form': form})

class ItineraryDeleteView(DeleteView):
    model = Itinerary
    template_name = "itineraries/delete_itinerary.html"
    success_url = reverse_lazy('itineraries')


class ItineraryUpdateView(UpdateView):
    model = Itinerary
    form_class = ItineraryForm
    template_name = "itineraries/edit_itinerary.html"
    success_url = reverse_lazy('itineraries')




