from django.conf.urls import url, patterns

urlpatterns = patterns('ipay.views',
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^payment/create/$', 'create_payment', name='create_payment'),
    url(r'^payment/(?P<pk>[\d]+)/$', 'edit_payment', name='edit_payment'),
)
