from django.conf.urls import url
from heroes import views

urlpatterns = [
	url(r'^heroes/$', views.heroes, name='heroes'),
    url(r'^heroes/(?P<slug>[\w-]+)/$', views.hero_profile, name='hero_profile'),
    url(r'^heroes/(?P<slug>[\w-]+)/(?P<link>[\w-]+)/$', views.trip_details, name='trip_details'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', views.trip_delete),
]