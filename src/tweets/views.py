from django.core.urlresolvers import reverse_lazy
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TweetModelForm
from .models import Tweet

from django.db.models import Q

from .mixin import FormUserNeededMixin, UserOwnerMixin

class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = "/tweet/create/"
    login_url = "/admin/"

class TweetUpdateView(UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = "/tweet/"

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get('pk')
    #     return Tweet.objects.get(pk=pk)

class TweetListView(ListView):

    template_name = 'tweets/tweet_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query)
                           | Q(user__username__icontains=query))
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context

class TweetDeleteView(UserOwnerMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list")


# #Retrieve
# def tweet_detail_view(request, id='1'):
#     obj = Tweet.objects.get(id=id)
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/tweet_detail.html", context)
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/tweet_list.html", context)