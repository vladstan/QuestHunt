from django.conf.urls import url
from tribes import views

from .views import UserSubcribeTribeView

urlpatterns = [
    url(r'^tribes/(?P<link>[\w|-]+)/$', views.tribe, name='tribe'),
    url(r'^tribes/(?P<link>[\w|-]+)/subscribe$', UserSubcribeTribeView.as_view(), name='subscribe'),
    url(r'^tribes/$', views.tribes, name='tribes'),
]