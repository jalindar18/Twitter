from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet/',views.twitter, name='tweet'),
    path('<int:tweet_id>/',views.favorite, name='favorite'),
    path('tweet/remove/<int:tweet_id>/',views.remove, name='remove'),
    path('tweet/update/<int:tweet_id>/', views.update_tweet, name='update_tweet'),
    path('tweet/dislike/<int:tweet_id>/', views.dislike, name='dislike'),
]