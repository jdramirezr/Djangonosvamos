import json
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import View

from django.http import JsonResponse


from app.models import Trip
from app.models import User
from app.models import Client
# Create your views here.


class TripDetailview(DetailView):
    model = Trip
    template_name = 'trip_detail.html'


class TripListView(ListView):
    model = Trip
    template_name = 'trip_list.html'
    http_method_names = ['post', 'get']

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        travel_date = request.POST.get('travel_date', '')
        city_from = request.POST.get('city_from', '')
        city_to = request.POST.get('city_to', '')
        quotas = request.POST.get('quotas', '')

        trip_queryset = Trip.objects.filter()

        if travel_date:
            trip_queryset = trip_queryset.filter(travel_date__date=travel_date)

        if city_from:
            trip_queryset = trip_queryset.filter(city_from=int(city_from))

        if city_to:
            trip_queryset = trip_queryset.filter(city_to=int(city_to))

        if quotas:
            trip_queryset = trip_queryset.filter(quotas__gte=int(quotas))

        response_json = []

        for trip in trip_queryset:
            response_json.append({
                'city_from': trip.get_city_from_display(),
                'city_to': trip.get_city_to_display(),
                'driver_id': trip.driver_id,
                'quotas': trip.quotas,
                'travel_date': trip.travel_date.date(),
                'price': trip.price,
            })

        return JsonResponse({
            'ok': True,
            'response': response_json,
            'type': 'success',
        })


class LoginView(ListView):
    model = Trip
    http_method_names = ['post', 'get']

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = User.objects.filter(
            username=username,
        ).first()

        if user and user.check_password(password):
            return JsonResponse({
                'ok': True,
                'user_id': user.id,
                'response': 'logueado correctamente, redirigiendo....',
            })

        return JsonResponse({
            'ok': False,
            'response': 'El usuario no existe',
        })


class CreateView(View):
    model = Trip
    http_method_names = ['post']

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        username = request.POST.get('username', '')
        password = request.POST.get('password1', '')

        user, create = User.objects.get_or_create(
            username=username,
        )

        if user and create:
            user.set_password(password)
            user.save()

            Client.objects.create(
                user=user,
                name=username,
                email=user.email,
                is_driver=False
            )
            return JsonResponse({
                'ok': True,
                'response': 'usuario creado correctamente, redirigiendo....',
            })

        return JsonResponse({
            'ok': False,
            'response': 'Ya existe un usuario con estos datos',
        })


class PostTripView(View):
    model = Trip
    http_method_names = ['post']

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        travel_date = request.POST.get('travel_date', '')
        city_from = request.POST.get('city_from', '')
        city_to = request.POST.get('city_to', '')
        quotas = request.POST.get('quotas', '')
        trip_price = request.POST.get('trip-price', '')
        if (
            travel_date and
            city_from and
            city_to and
            quotas and
            trip_price and
            trip_price.isdigit()
        ):
            Trip.objects.create(
                travel_date=travel_date,
                driver_id=Client.objects.order_by('?').first().id,
                city_from=city_from,
                city_to=city_to,
                quotas=quotas,
                price=int(trip_price),
            )

            return JsonResponse({
                'ok': True,
                'response': 'Se ha publicado tu viaje, redirigiendo....',
            })

        return JsonResponse({
            'ok': False,
            'response': 'No se ha creado el viaje, revisa el precio',
        })
