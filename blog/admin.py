from django.contrib import admin
from blog.models import Article, Comment, Tag, ArticleTag
from mysite.models import User, Profile

class ArticleTagInline(admin.TabularInline):
  model = ArticleTag
  extra = 1

class ArticleUserInline(admin.TabularInline):
  model = User
  extra = 2

class ArticleAdmin(admin.ModelAdmin):
  inlines = [ArticleTagInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
