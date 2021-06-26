from django import forms
from .models import Order
from authentication.models import CustomUser 
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['user', 'book', 'plated_end_at']
        widgets = {'plated_end_at': DateInput()}


    def clean(self):
        return self.cleaned_data

class UpdateOrderForm(OrderForm):
    
    def clean(self):
        user =  self.cleaned_data['user']
        book = self.cleaned_data['book']
        plated_end_at = self.cleaned_data['plated_end_at']
        return self.cleaned_data