from django import forms
from .models import Thing

"""Forms of the project."""
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput()
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 35:
            raise forms.ValidationError("Ensure this value has at most 35 characters.")
        return name

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0 or quantity > 50:
            raise forms.ValidationError("Quantity must be between 0 and 50.")
        return quantity
