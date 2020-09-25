"""tpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from hashtag.views import list_view, home_view, spam_tweets_view, add_spam_tweets, detail
from authentication.views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_view, name='home'),
    path('result/<int:id>', detail, name="detail"),
    path('add/', add_spam_tweets, name='add'),
    path('hashtag/', list_view, name='hashtag'),
    path('result/', spam_tweets_view, name='result'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")

]
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
