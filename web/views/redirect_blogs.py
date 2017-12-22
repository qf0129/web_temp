from django.conf.urls import url
from aldryn_newsblog.models import ArticleTranslation
from django.shortcuts import redirect

def add_blog_urls(urlpatterns):
    arts = ArticleTranslation.objects.all()
    for art in arts:
        urlpatterns.append(url(r'^' + art.slug + '/', redirect_blog_url))

def redirect_blog_url(request):
    return redirect('/blog/' + request.path.replace('/', ''))