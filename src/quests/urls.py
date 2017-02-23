from django.conf.urls import url
from quests import views



urlpatterns = [
    url(r'^quests/(?P<slug>[\w-]+)/$', views.quest_details, name='quest_details'),
    url(r'^quests/$', views.quests, name='quests'),
]