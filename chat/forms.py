from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    # review = forms.Charfield()
    class Meta:
        model = Contact
        # fields = ['name', 'email', 'type', 'comment']
        fields = "__all__"