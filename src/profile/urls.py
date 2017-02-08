from django.conf.urls import url
from profile import views

urlpatterns = [
    url(r'^experts/(?P<slug>[\w-]+)/$', views.expert_profile, name='expert_profile'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', views.trip_delete),
]