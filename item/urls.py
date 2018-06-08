# import function url()
from django.conf.urls import url

from . import views

# route setting
urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
]
