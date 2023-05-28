from django import forms
from django.forms import DateInput
from .models import *

class ItineraryForm(forms.ModelForm):
    destinations = forms.ModelMultipleChoiceField(queryset=Destination.objects.all(), widget=forms.CheckboxSelectMultiple, required=False, to_field_name='name')
    accommodations = forms.ModelMultipleChoiceField(queryset=Accommodation.objects.all(), widget=forms.CheckboxSelectMultiple, required=False, to_field_name='name')
    startDate = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    finishDate = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Itinerary
        fields = ['name', 'description', 'startDate', 'finishDate', 'destinations', 'accommodations']

    def clean(self):
                    cleaned_data = super().clean()
                    destinations = cleaned_data.get('destinations')
                    accommodations = cleaned_data.get('accommodations')

                    startDate = cleaned_data.get('startDate')
                    finishDate = cleaned_data.get('finishDate')

                    if startDate and finishDate and startDate > finishDate:
                       self.add_error('finishDate',"Start date has to be after to the end date")

                    id_citys = list(map(lambda destination: destination.id, destinations))
                    result = all(accommodation.destination.id in id_citys for accommodation in accommodations)

                    if not result:
                        self.add_error('accommodations', "Invalid accommodation")

                    return cleaned_data




