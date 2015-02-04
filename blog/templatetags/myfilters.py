__author__ = 'boshepelinski'
from django import template

from blog.views import AllTagCloudView
from blog.models import Tag
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('tag_cloud.html', takes_context=True)
def sidebar_sorted_tags(context):
    """
    The sidebar with the sorted tags.
    """
    return {'tag_cloud': Tag.objects.values("name", "slug")
            .annotate(Count("post")).order_by('-post__count')}
