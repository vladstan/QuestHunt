from django.conf.urls import url
from trips import views

urlpatterns = [
    url(r'^trips/$', views.trips_list, name='trips_list'),
    url(r'^experiences/(?P<link>[\w|-]+)/$', views.category, name='category'),
    url(r'^trips/(?P<slug>[\w-]+)/$', views.trip_details, name='trip_details'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', views.trip_delete),
]