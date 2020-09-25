from django.forms import ModelForm
from . models import Hashtag, SpamTweets


class HashtagForm(ModelForm):
    class Meta:
        model = Hashtag
        fields = ['hashtag', 'tweets_colected',
                  'per_of_spammer', 'spammer_found']


class Spam_Tweets_Form(ModelForm):
    class Meta:
        model = SpamTweets
        fields = ['hashtag', 'msg_id',
                  'user_id', 'name', 'location', 'slug']
