from django.conf.urls import url
from masters import views

urlpatterns = [
    url(r'^masters/$', views.masters, name='masters'),
    #url(r'^masters/(?P<slug>[\w-]+)/$', views.master_profile, name='master_profile'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', views.trip_delete),
]