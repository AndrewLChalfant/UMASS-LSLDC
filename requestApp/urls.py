from django.db import models
from django.conf.urls import url
from . import views 
from django.views.generic import TemplateView

#SITE URL MAPPINGS
urlpatterns= [
    url(r'^$', views.home, name='home'),
    url(r'^employee_complete/$', views.complete, name='complete'),
	url(r'^manager_complete/$', views.manager_complete, name='manager_approved'),
    url(r'^colo/$', views.COLO, name= 'colo'),
    url(r'^login/$', views.login, name= 'login'),
url(r'^manager_confirm/(?P<token>[0-9A-Za-z]{1,3}-[0-9A-Za-z]{1,20})/(?P<uuid4>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', views.manager, name='manager'),
    ]
