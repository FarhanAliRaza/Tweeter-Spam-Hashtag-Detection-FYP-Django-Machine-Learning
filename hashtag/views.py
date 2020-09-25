from django.shortcuts import render
from .hashtag import get_hashtag
from .forms import HashtagForm, Spam_Tweets_Form
from .models import Hashtag, SpamTweets
from django.contrib.auth.decorators import login_required
from data import result
from django.shortcuts import redirect


def getavg():
    obj_list = Hashtag.objects.all()
    total_groups = len(obj_list)
    ttc = 0
    tsf = 0
    for obj in obj_list:
        ttc += obj.tweets_colected
        tsf += obj.spammer_found
    ex = {
        "total_groups": total_groups,
        "total_tweets": ttc,
        "total_spam_tweets": tsf,
        "total_spam_per": tsf/ttc*100,
    }
    return ex


def home_view(request):
    obj = result.get_hashtag()
    form = HashtagForm(request.POST or None)
    try:
        f = form.save(commit=False)
        f.hashtag = obj['name']
        f.tweets_colected = obj['total']
        f.spammer_found = obj['spammer']
        f.per_of_spammer = obj['per']
        f.save()
    except:
        pass
    objects = Hashtag.objects.all()
    ex = getavg()
    context = {
        "total": ex,
        'obj_list': objects
    }
    template_name = 'index.html'
    return render(request, template_name, context)


def list_view(request):
    try:
        obj_list = get_hashtag()
        name_list = []
        for obj in obj_list:
            name_list.append(obj['name'])
        t = len(name_list) + 1
        context = {
            'obj_list': obj_list,
            't': t,
        }
        template_name = 'tables.html'
        return render(request, template_name, context)
    except:
        return render(request, "error.html", context={})


def spam_tweets_view(request):
    list_of_tweets = result.get_spam_tweets()
    objects = Hashtag.objects.all()
    ex = getavg()
    context = {
        "total": ex,
        'hashtag_list': objects,
        'tweets_list': list_of_tweets
    }
    template_name = 'spam_tweets.html'
    return render(request, template_name, context)


def detail(request, id):
    obj_list = SpamTweets.objects.filter(hashtag=id)
    print(obj_list)
    context = {
        "obj_list": obj_list
    }
    template_name = 'icons.html'
    return render(request, template_name, context)


@login_required(login_url="/login/")
def add_spam_tweets(request):
    list_of_tweets = result.get_spam_tweets()
    form = Spam_Tweets_Form(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            hashtag = form.cleaned_data.get("hashtag")
            slug = form.cleaned_data.get("slug")
            for obj in list_of_tweets:
                msg_id = obj['msg_id']
                user_id = obj['user_id']
                name = obj['screen_name']
                location = obj['location']
                t = SpamTweets(hashtag=hashtag, msg_id=msg_id,
                               user_id=msg_id, name=name, location=location, slug=slug)
                t.save()
            msg = "Successful"
            return redirect("result")
    context = {
        'form': form,
        'msg': msg
    }
    template_name = 'form.html'
    return render(request, template_name, context)
