from django.conf.urls.defaults import *


urlpatterns = patterns('outlets.views',
    url(r'^$', 'index', name='outlets-index'),
)