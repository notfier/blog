from django.conf.urls import patterns, url

from blog.views import PostsList, SinglePost, TagView, AllTagCloudView
# urls

urlpatterns = patterns('',
    url(r'^$', PostsList.as_view(), name="all_posts"),
    url(r'^post/(?P<slug>\w+)/$', SinglePost.as_view(),
                                    name='single_post'),
    url(r'^tag/(?P<slug>\S+)/$', TagView.as_view(),
                                    name='tagger'),
    url(r'^post/add_comment/(?P<slug>\S+)/$', 'blog.views.add_comment',
                                    name="commenter")
)