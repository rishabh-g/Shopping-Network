from django.conf.urls import patterns, url

from hyd_smartshop import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
#	url(r'^p1_submit/$', views.p1_submit, name='index'),
	url(r'^login', views.login, name='login'),
	url(r'^signin$', views.signin, name='signin'),
	url(r'^signup$', views.signup, name='signup'),
)
