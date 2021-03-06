from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'awsomer.views.home', name='home'),
    url(r'^cloudfront/', include('cloudfront.urls')),
    url(r'^ec2/', include('ec2.urls')),
    url(r'^route53/', include('route53.urls')),
    url(r'^rds/', include('rds.urls')),
    url(r'^sqs/', include('sqs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
