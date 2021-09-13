from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Article, Category
from django.core.paginator import Paginator
# Create your views here.

def index(request, page=1):
	articles_list = Article.objects.published()
	pagiator = Paginator(articles_list, 1)
	articles = pagiator.get_page(page)
	context = {
		"articles": articles,
	}

	return render(request, 'blog/home.html', context)


def detail(request, slug):
	context = {
		"art": get_object_or_404(Article.objects.published(), slug=slug)
	}
	return render(request, 'blog/detail.html', context)


def category(request, slug, page=1):
	category = get_object_or_404(Category, slug=slug, status=True)
	articles_list = category.articles.published()
	pagiator = Paginator(articles_list, 1)
	articles = pagiator.get_page(page)
	context = {
		"articles": articles,
		"category": category
	}

	return render(request, 'blog/category.html', context)