from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/customers$', views.customer),
]
