from django.conf.urls import patterns, url

from blog.views import PostsList, SinglePost, TagView, AllTagCloudView
from test_blog.settings import MEDIA_ROOT
# urls


urlpatterns = patterns('',
    url(r'^tag/(?P<slug>\S+)/$', TagView.as_view(),
                                    name='tagger'),
    url(r'^post/add_comment/(?P<slug>\S+)/$',
        'blog.views.add_comment', name="commenter"),
    url(r'^$', PostsList.as_view(), name="all_posts"),
    url(r'^post/(?P<slug>\S+)/$', SinglePost.as_view(),
                                    name='single_post'),
)

urlpatterns += patterns('',
    url(r'^media/pictures/(.+)/$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT, }),
)