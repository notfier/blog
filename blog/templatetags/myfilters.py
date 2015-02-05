__author__ = 'boshepelinski'
from django import template
from django.db.models import Count

from blog.models import Tag


register = template.Library()


@register.inclusion_tag('tag_cloud.html', takes_context=True)
def sidebar_sorted_tags(context):
    """
    The sidebar with the sorted tags.
    """
    return {'tag_cloud': Tag.objects.values("name", "slug")
            .annotate(Count("post")).order_by('-post__count')}


@register.filter(name="addclass")
def add_class(val, arg):
    """
    Add classes to form elements.
    """
    return val.as_widget(attrs={"class": arg})
