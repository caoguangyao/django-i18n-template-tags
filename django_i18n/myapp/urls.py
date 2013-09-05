from django.conf.urls.defaults import *
from views import index_view

urlpatterns = patterns(
        '',
        (r'^index/$',index_view),
        )
