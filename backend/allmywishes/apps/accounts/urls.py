from django.conf.urls import patterns, url

from wish import views as wish_views

urlpatterns = patterns(
    'accounts.views',

    url(r'^info$', 'account_info', name="account-info"),
    url(r'^connect$', 'account_connect', name="account-connect"),
    url(r'^logout$', 'account_logout', name='account-logout'),

    # Wishes
    url(r'^(?P<slug>[\w-]+)$', 'account_details', name='account-details'),
    url(r'^(?P<slug>[\w-]+)/wishes$', wish_views.wish_list_create, name='wish-list-create'),
    url(r'^(?P<slug>[\w-]+)/wishes/(?P<pk>[\w-]+)$', wish_views.wish_retrieve, name='wish-retrieve'),
)
