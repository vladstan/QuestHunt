from django.conf.urls import url
from quests import views

from .views import UserSubcribeTribeView


urlpatterns = [
    url(r'^quests/$', views.quests_list, name='quests_list'),
    url(r'^tribes/(?P<link>[\w|-]+)/$', views.tribe, name='tribe'),
    url(r'^tribes/(?P<link>[\w|-]+)/subscribe$', UserSubcribeTribeView.as_view(), name='subscribe'),
    url(r'^quests/(?P<slug>[\w-]+)/$', views.quest_details, name='quest_details'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', views.trip_delete),
]