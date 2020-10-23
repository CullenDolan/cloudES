from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# what to save to the db


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    
    # function to redirect user after creating a blog post
    # reverse: return full url to route as a string
    # view will handle the redirect
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})