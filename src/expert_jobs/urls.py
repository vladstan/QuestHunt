from django.conf.urls import url
from expert_jobs import views

urlpatterns = [
    url(r'^travel-expert-jobs/$', views.landing, name='landing'),
]