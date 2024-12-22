from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Article, Comment, Tag
from blog.forms import CommentForm
from django.core.paginator import Paginator

def index(request):
  objs = Article.objects.all().select_related('user__profile')
  paginator = Paginator(objs, 2)
  page_number = request.GET.get('page')
  context = {
    'title': 'ブログ一覧',
    'page_obj': paginator.get_page(page_number),
    'page_number': page_number
  }
  return render(request, 'blog/blogs.html', context)

def article(request, pk):
  
  obj = Article.objects.get(pk=pk)

  if request.method == 'POST':
    if request.POST.get('like_count', None):
      obj.count += 1
      obj.save()
    else:
      form = CommentForm(request.POST)
      if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = obj
        comment.save()

  comments = Comment.objects.filter(article=obj).select_related('user__profile')
  context = {
    'article': obj,
    'comments': comments
  }
  return render(request, 'blog/article.html', context)

def tags(request, slug):
  tag = Tag.objects.get(slug=slug)
  articles = tag.article_set.all().select_related('user__profile')
  paginator = Paginator(articles, 2)
  page_number = request.GET.get('page')
  context = {
    'title': '#タグ',
    'page_obj': paginator.get_page(page_number),
    'page_number': page_number
  }
  return render(request, 'blog/blogs.html', context)
