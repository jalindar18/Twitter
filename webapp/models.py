from django.db import models
from django.contrib.auth.admin import User

class tweettable(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.TextField()
    is_liked = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


class favtable(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey(tweettable, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

