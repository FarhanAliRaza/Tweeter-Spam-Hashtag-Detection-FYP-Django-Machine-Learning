from django.db import models

# Create your models here.


class Hashtag(models.Model):
    hashtag = models.CharField(max_length=255, unique=True, default='test')
    tweets_colected = models.PositiveIntegerField(default=20)
    spammer_found = models.PositiveIntegerField(default=0)
    per_of_spammer = models.CharField(max_length=20, default='0.0%')

    def __str__(self):
        return self.hashtag


class SpamTweets(models.Model):
    hashtag = models.ForeignKey(
        Hashtag, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    msg_id = models.PositiveIntegerField(default=000, blank=True, null=True)
    user_id = models.PositiveIntegerField(default=0000, blank=True, null=True)
    name = models.CharField(
        default='none', max_length=255, blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=255)
