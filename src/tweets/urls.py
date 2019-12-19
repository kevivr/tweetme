from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    RetweetView,
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
)


urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),# /tweet/
    url(r'^search/$', TweetListView.as_view(), name='list'),# /tweet/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), #/tweet/[id]
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'), #/tweet/[id]
    url(r'^create/$', TweetCreateView.as_view(), name='create'),# /tweet/create
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), #/tweet/[id]/update
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete') #/tweet/[id]/delete
]
