from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from hyd_smartshop import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#import django_cron
#django_cron.autodiscover()


urlpatterns = patterns('',

	 url(r'^$', views.index, name='index'),
	  # Login / logout.
#    (r'^login/$', 'django.contrib.auth.views.login'),
#    (r'^logout/$', logout_page),

    # Examples:
    # url(r'^$', 'mcq.views.home', name='home'),
    # url(r'^mcq/', include('mcq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^hyd_smartshop/', include('hyd_smartshop.urls', namespace="hyd_smartshop")),

  # Serve static content.
 #   (r'^static/(?P<path>.*)$', 'django.views.static.serve',
  #      {'document_root': 'static'}),

)
