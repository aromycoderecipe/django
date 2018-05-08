from django.conf.urls import url
# from blog import views
from . import views


urlpatterns = [
    url(r'^$', views.post_list,name='post_list'),
    # localhost:
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]