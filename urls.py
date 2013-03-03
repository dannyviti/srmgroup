from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^srmgroup/', include('srmgroup.foo.urls')),
	(r'^customer/login/$', login),
	(r'^customer/$', login),
	(r'^customer/logout/$', logout),
	(r'^files/$', 'customer_portal.views.file_index'),
	(r'^srmgroup/adminfiles/(?P<filename>.*)$', 'customer_portal.views.sendfile', {'path':'/home/django_code/media/srmgroup/media_upload/srmgroup/adminfiles/'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    (r'^admin/', include(admin.site.urls)),
	(r'^adminfiles/', include('adminfiles.urls')),
	(r'^', include('sorl.thumbnail.urls')),
)
