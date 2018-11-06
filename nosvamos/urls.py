from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from app.views import TripListView
from app.views import TripDetailview
from app.views import LoginView
from app.views import CreateView
from app.views import PostTripView

urlpatterns = [
    url(
        r'^listado-viajes/$',
        TripListView.as_view(),
        name='trip_list'
    ),
    url(
        r'^login/$',
        LoginView.as_view(),
        name='login'
    ),
    url(
        r'^create/$',
        CreateView.as_view(),
        name='create'
    ),
    url(
        r'^post_trip/$',
        PostTripView.as_view(),
        name='post_trip'
    ),

    url(
        r'^detalle-viaje/(?P<pk>[0-9a-zA-Z]+)/$',
        TripDetailview.as_view(),
        name='trip_detail'
    ),
    url(r'^admin/', admin.site.urls),
]
