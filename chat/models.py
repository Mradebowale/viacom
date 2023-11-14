from django.db import models
from django.utils import timezone

# Create your models here.

CONTACT_TYPE = (
    ("Inquiry", "Inquiry"),
    ("Compliant", "Complaint"),
)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(help_text="Insert a valid email")
    type = models.CharField(max_length=10, choices= CONTACT_TYPE)
    message = models.TextField(max_length=7000)
    date_time = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name