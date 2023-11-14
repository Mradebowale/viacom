from .views import Contact, contact2
from django.urls import path




urlpatterns = [

    path('', Contact),
    path('contact/', contact2, name='contact'),
]





