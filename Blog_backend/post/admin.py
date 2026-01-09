from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ['id', 'image', 'title', 'content', 'user_id', 'timestamp', 'last_updated', 'views', 'likes']
    readonly_fields = ['id', 'timestamp', 'last_updated']
    list_display = ['id', 'user_id', 'title', 'timestamp', 'post_like']
    list_filter = ['user_id', 'timestamp', 'last_updated', 'views', 'likes']
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    fields = ['id', 'post_id', 'content', 'user_id', 'likes']
    readonly_fields = ['id']
    list_display = ['id', 'post_id', 'user_id', 'comment_like']
    list_filter = ['post_id', 'likes']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
