from django.conf.urls import url
from django.urls import path
from .views import serve_docs


urlpatterns = [
    url(r'^(?P<path>.*)$', serve_docs),
]