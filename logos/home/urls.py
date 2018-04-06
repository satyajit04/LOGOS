from django.conf.urls import url, include
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jute_products/$', views.padukaindex, name='jute_products'),
    url(r'^strategy_&_consultancy/$', views.strategy_index, name='strategy'),
    url(r'^electrical_&_electronics/$', views.eee_index, name='eee'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
]
