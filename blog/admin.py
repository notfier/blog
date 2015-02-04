from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'added', 'comment_text']




