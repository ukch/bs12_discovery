from django.conf.urls import patterns, include, url

from .api import v1_api

urlpatterns = patterns("bs12_discovery.views",
        url("^$", "index"),
        url(r'^api/', include(v1_api.urls)),
)
