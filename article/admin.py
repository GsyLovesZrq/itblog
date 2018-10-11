from django.contrib import admin
from .models import ArticleColumn,Comment

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'created', 'user')
    list_filter = ("column",)

admin.site.register(ArticleColumn, ArticleColumnAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','body','commentator')
    list_filter = ('article','commentator','body')
    search_fields = ('body',)
admin.site.register(Comment,CommentAdmin)