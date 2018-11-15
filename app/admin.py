from django.contrib import admin
from app.models import Trip
from app.models import Reservation
from app.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'is_driver',
    )


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        'travel_date',
        'quotas',
        'driver',
        'city_from',
        'city_to',
        'price',
    )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'trip',
        'user',
        'requested_quotas',
    )



