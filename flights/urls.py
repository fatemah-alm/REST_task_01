from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('flights-list/', views.flights, name='flights-list'),
    path('bookings/', views.bookings, name='bookings-list' )
]