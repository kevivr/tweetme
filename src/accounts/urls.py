from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
   UserDetailView,
   UserFollowView
)


urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),# /tweet/
    # url(r'^search/$', TweetListView.as_view(), name='list'),# /tweet/
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), #/tweet/[id]
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow')
    # url(r'^create/$', TweetCreateView.as_view(), name='create'),# /tweet/create
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), #/tweet/[id]/update
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete') #/tweet/[id]/delete
]
