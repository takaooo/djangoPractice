from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    # eg: /polls/
    url(r'^$', views.index, name='index'),
    # eg: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # eg: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # eg: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)