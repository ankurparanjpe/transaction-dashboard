from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^internal_delay/$', views.internal_delay, name='internal_delay'),
    url(r'^sales_overview/$', views.sales_overview, name='sales_overview'),
    url(r'^invoices_missing/$', views.invoices_missing, name='invoices_missing'),
    url(r'^delivery_chain_problem/$', views.delivery_chain_problem, name='delivery_chain_problem'),
    url(r'^external_delay/$', views.external_delay, name='external_delay'),
    url(r'^project_performance/$', views.offer_missing, name='offer_missing'),
    url(r'^example/$', views.example, name='example'),
]
