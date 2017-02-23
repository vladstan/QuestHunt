from django.conf.urls import url
from destinations import views


urlpatterns = [  
    url(r'^destinations/(?P<link>[\w|-]+)/$', views.destination, name='destination'),
    url(r'^destinations/$', views.destinations, name='destinations'),
]