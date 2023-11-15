from .views import contact, contact2, contact3
from django.urls import path




urlpatterns = [

    path('', contact),
    path('contact/', contact2, name='contact'),
    path("contact3",contact3, name='contact3' )
]





