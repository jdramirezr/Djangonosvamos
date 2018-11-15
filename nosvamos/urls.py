from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from app.views import TripListView
from app.views import TripDetailview
from app.views import LoginView
from app.views import CreateView
from app.views import PostTripView

urlpatterns = [
    path(
        'listado-viajes/',
        TripListView.as_view(),
        name='trip_list'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'create/',
        CreateView.as_view(),
        name='create'
    ),
    path(
        'post_trip/',
        PostTripView.as_view(),
        name='post_trip'
    ),

    path(
        'detalle-viaje/<int:pk>/',
        TripDetailview.as_view(),
        name='trip_detail'
    ),
    path('admin/', admin.site.urls),
]
