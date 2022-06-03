from django import forms
from .models import Item

# Create a class that inherits all the functionality of forms.ModelForm
class ItemForm(forms.ModelForm):
    # The Meta class tells the form which model the form is to be associated with,
    # what fields it should render, how it should display error messages, etc.
    class Meta:
        model = Item
        fields = ['name', 'done']
