from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_protect
from django.db.models import Count

from blog.models import Post, Tag, Comments
from blog.forms import CommentForm


# Create your views here.


class PostsList(ListView):
    model = Post
    context_object_name = 'posts_list'
    template_name = 'posts.html'
    paginate_by = 5


class SinglePost(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        comment_form = CommentForm
        context = super(SinglePost, self).get_context_data(**kwargs)
        comments = Comments.objects.filter(comment_id=self.object).order_by('-added')
        context['comments'] = comments
        context['form'] = comment_form
        return context


class TagView(ListView):
    model = Tag
    template_name = 'tag.html'
    context_object_name = 'tag_list'
    paginate_by = 5

    def get_queryset(self):
        slug_received = self.kwargs['slug']
        tag = get_object_or_404(Tag, slug=slug_received)
        return tag.post_set.all().order_by('-posted')

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        slug_received = self.kwargs['slug']
        tags = get_object_or_404(Tag, slug=slug_received)
        context['posts'] = tags
        return context


class AllTagCloudView(ListView):
    model = Tag
    template_name = 'tag_cloud.html'
    context_object_name = 'tag_cloud'

    def get_queryset(self):
        qs = Tag.objects.values("name", "slug")\
            .annotate(Count("post")).order_by('-post__count')
        return qs


@csrf_protect
def add_comment(request, slug):
    """
    Add comment to.
    """
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment = Post.objects.get(slug=slug)
            form.save()
    return redirect('/post/{0}/'.format(slug))





