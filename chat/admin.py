from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "type", "date_time", "date_updated"]
    list_filter = ["name", "email", "type", "date_time"]
    search_fields = ["name", "email"]
    list_editable = ["email", "type"]


admin.site.register(Contact, ContactAdmin)