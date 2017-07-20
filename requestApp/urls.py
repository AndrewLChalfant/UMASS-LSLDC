from django.db import models
from django.conf.urls import url
from . import views 
from django.views.generic import TemplateView

#SITE URL MAPPINGS
urlpatterns= [
    url(r'^$', views.home, name='home'),
    url(r'^employee_complete/$', views.complete, name='complete'),
    url(r'^supervisor_confirm/$', views.manager, name='supervisor'),
	url(r'^supervisor_complete/$', views.supervisor_complete, name='supervisor_approved'),
    url(r'^employee_verify/$', views.employee_info, name='incomplete'),
    url(r'^colo/$', views.COLO, name= 'colo'),
    url(r'^login/$', views.login, name= 'login'),
    ]
