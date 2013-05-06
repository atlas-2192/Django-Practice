from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^djproject/', include('djproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    (r'^admin/', include(admin.site.urls)),
    
    (r'^jobs/$', 'djproject.jobs.views.index'),
    (r'^json/$', 'djproject.jobs.views.json'),
    (r'^menus/$', 'djproject.jobs.views.menus'),
    (r'^menus/contact_new', 'djproject.jobs.views.contact'),
    (r'^jobs/(?P<job_id>\d+)/$', 'djproject.jobs.views.detail'),
    (r'^jobs/', include('djproject.jobs.urls')),
)

urlpatterns += staticfiles_urlpatterns()