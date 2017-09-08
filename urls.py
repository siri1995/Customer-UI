from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CustomerList.as_view(), name='customer-list'),
    url(r'customer/add/$', views.CustomerAddressCreate.as_view(), name='customer-add'),
    url(r'customer/(?P<pk>[0-9]+)/$', views.CustomerAddressUpdate.as_view(), name='customer-update'),
    url(r'customer/(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='customer-delete'),
]