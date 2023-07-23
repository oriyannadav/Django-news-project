from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)

    @property
    def number_of_comments(self):
        return NewsComment.objects.filter(newsStory_connected=self).count()

class NewsComment(models.Model):
    newsStory_connected = models.ForeignKey(
        NewsStory, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.newsStory_connected.title[:40]