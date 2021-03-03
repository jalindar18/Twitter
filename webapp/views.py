from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import tweettable, favtable
from .forms import register_form, twitter_form, edit_form

@login_required
def index(request):
    username = None
    AllTweets = tweettable.objects.all()
    AllTweets1 = tweettable.objects.all().values_list('id', flat=True)
    AllTweetsLikes = favtable.objects.filter(pk__in=AllTweets1).count()
    SelfTweet = 'Tweets not available.'
    LikedTweet = 'Tweets not available'
    try:
        username = User.objects.get(username=request.user.username)
        SelfTweet = tweettable.objects.filter(user=request.user)
        likedtweetid = favtable.objects.filter(user=request.user).values_list('tweet', flat=True)
        LikedTweet = tweettable.objects.filter(pk__in=likedtweetid)



    except User.DoesNotExist:
        return render(request,'webapp/index.html',{'SelfTweet':SelfTweet,'LikedTweet':LikedTweet,'AllTweets':AllTweets,'AllTweetsLikes':AllTweetsLikes})

    return render(request, 'webapp/index.html',{'SelfTweet': SelfTweet, 'LikedTweet': LikedTweet, 'AllTweets': AllTweets, 'username':username,'AllTweetsLikes':AllTweetsLikes})

def register_user(request):

    if request.method == 'POST':

        form = register_form(request.POST)

        if form.is_valid():

            user1 = form.save(commit=False)
            user1.set_password(user1.password)
            user1.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request,user)
                return redirect('index')
    else:

        form = register_form()

    return render(request, 'webapp/register.html',{'form':form})

@login_required
def twitter(request):

    if request.method == 'POST':
        form = twitter_form(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('index')
    else:
        form = twitter_form()
    return render(request, 'webapp/twitter.html', {'form': form})

@login_required
def update_tweet(request, tweet_id):
    data = tweettable.objects.get(pk=tweet_id)
    if request.method == 'POST':
        form = twitter_form(request.POST, instance=data)
        form.instance.user = request.user

        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('index')
    else:
        form = twitter_form()
    return render(request, 'webapp/post_edit.html', {'form': form})


def favorite(request,tweet_id):
    msg = None
    new_like ,created = favtable.objects.get_or_create(user=request.user, tweet_id=tweet_id)
    if created is False:
        msg = 'You already liked this Tweet'
        #return render(request, 'webapp/index.html', {'msg': msg})
    return render(request, 'webapp/index.html', {'msg': msg})


def remove(request, tweet_id):

    tweettable.objects.filter(pk=tweet_id).delete()
    return redirect('index')

def dislike(request, tweet_id):
    dislike = favtable.objects.filter(user=request.user, tweet_id=tweet_id).delete()
    return redirect('index')