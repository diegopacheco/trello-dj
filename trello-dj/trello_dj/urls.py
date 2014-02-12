from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^example', 'example.views.hello'),
	url(r'^burndown', 'example.views.burndown'),
    url(r'^range/from/(\d{2}-[aA-zZ]{3}-\d{4})/to/(\d{2}-[aA-zZ]{3}-\d{4})/$','example.views.date'),
)
