from django.conf.urls.defaults import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': "/Users/johnsietsma/envs/corpse/lib/python2.7/site-packages/django/contrib/admin/media/"}),    
        
    (r'site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^%s' % settings.URL_RE_ROOT, include('corpseflipper.urls')),        
)
