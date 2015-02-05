from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin


from . import models

# Register your models here.


@admin.register(models.Post)
class PostAdmin(MarkdownModelAdmin):
    list_display = ['title', 'posted']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'added', 'comment_text']




