from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.


class Tag(models.Model):
    """
    Tag.
    """
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('tagger', args=[str(self.slug)])

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Tag'


class Post(models.Model):
    """
    Post model.
    """

    title = models.CharField(max_length=50)
    posted = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=10000)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('single_post', args=[str(self.slug)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-posted']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'


class Comments(models.Model):
    """
    Comments model.
    """

    comment = models.ForeignKey(Post)
    author = models.CharField(max_length=30)
    added = models.DateTimeField(auto_now_add=True, default=timezone.now)
    comment_text = models.TextField(max_length=300)

    def __str__(self):
        return 'Added %r | %r'%(self.added, self.author)



