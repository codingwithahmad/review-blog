from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Article, Category
from account.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from account.mixins import AuthorAccessMixin
from django.db.models import Count, Q
from datetime import datetime, timedelta
from django.db.models import Q
# Create your views here.

# def index(request, page=1):
# 	articles_list = Article.objects.published()
# 	pagiator = Paginator(articles_list, 1)
# 	articles = pagiator.get_page(page)
# 	context = {
# 		"articles": articles,
# 	}

# 	return render(request, 'blog/home.html', context)


class ArticlesList(ListView):
	# model = Article
	queryset = Article.objects.published()
	paginate_by = 2

# def detail(request, slug):
# 	context = {
# 		"art": get_object_or_404(Article.objects.published(), slug=slug)
# 	}
# 	return render(request, 'blog/detail.html', context)

class ArticleDetail(DetailView):
	
	def get_object(self):
		slug = self.kwargs.get('slug')
		article = get_object_or_404(Article.objects.published(), slug=slug)

		ip_address = self.request.user.ip_address

		if ip_address not in article.hits.all():
			article.hits.add(ip_address)

		return article



class ArticlesPreview(AuthorAccessMixin, DetailView):
	
	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(Article, pk=pk)


# def category(request, slug, page=1):
# 	category = get_object_or_404(Category, slug=slug, status=True)
# 	articles_list = category.articles.published()
# 	pagiator = Paginator(articles_list, 1)
# 	articles = pagiator.get_page(page)
# 	context = {
# 		"articles": articles,
# 		"category": category
# 	}

# 	return render(request, 'blog/category.html', context)


class CategoryList(ListView):
	paginate_by = 1
	template_name = "blog/category_list.html"

	def get_queryset(self):
		global category
		slug = self.kwargs.get('slug')
		category = get_object_or_404(Category.objects.published(), slug=slug,)
		return category.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = category
		return context

class AuthorList(ListView):
	paginate_by = 1
	template_name = "blog/author_list.html"

	def get_queryset(self):
		global author
		username = self.kwargs.get('username')
		author = get_object_or_404(User, username=username)
		return author.articles.published()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['author'] = author
		return context


class SearchList(ListView):
	paginate_by = 1
	template_name = "blog/search_list.html"

	def get_queryset(self):
		search = self.request.GET.get('q')
		return Article.objects.filter(Q(description__icontains=search) | Q(description__icontains=search))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['search'] = self.request.GET.get('q')
		return context

