from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^predict/$',views.find_creditability, name='predict')
]