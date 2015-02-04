from django.forms import ModelForm
from django import forms
from django.forms import widgets

from blog.models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['author', 'comment_text']
        widgets = {
            'comment_text': widgets.Textarea(attrs=dict(required=True,))
        }