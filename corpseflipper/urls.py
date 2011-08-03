from django.views.generic.edit import CreateView
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from models import Corpse
#from views import CorpseView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^head/(?P<link_type>\d+)/$', 'corpseflipper.views.random_head'),    
    url(r'^create/', 'corpseflipper.views.create'),
    url(r'^', 'corpseflipper.views.random'),    
)
