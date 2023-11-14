from .models import Contact
from django import forms

CONTACT_TYPE = (
    ("Inquiry", "Inquiry"),
    ("Compliant", "Complaint"),
)

class ContactForm(forms.ModelForm):
    # review = forms.Charfield()
    class Meta:
        model = Contact
        # fields = ['name', 'email', 'type', 'comment']
        fields = "__all__"






class Contactform2(forms.Form):
    name = forms.CharField(max_length= 100)
    email = forms.EmailField()
    type = forms.ChoiceField(choices=CONTACT_TYPE)
    message = forms.CharField(widget=forms.Textarea)