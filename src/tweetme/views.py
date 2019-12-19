from django.shortcuts import render


#Retrieve
def tweet_detail_view(request, id=1):
    return render(request, "tweets/tweet_detail.html", {})

def tweet_list_view(request):
    return render(request, "tweets/tweet_list.html", {})

def home(request):
    return render(request, "home.html", {})