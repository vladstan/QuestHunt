from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^posts/$', views.posts_list, name='posts_list'),
    url(r'^quests/(?P<link>[\w|-]+)/$', views.category, name='category'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.post_details, name='post_details'),
	#url(r'^(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', views.trip_delete),
]