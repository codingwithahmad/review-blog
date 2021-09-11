from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Article, Category
# Create your views here.

def index(request):
	context = {
		"articles": Article.objects.published(),
	}
	return render(request, 'blog/home.html', context)


def detail(request, slug):
	context = {
		"art": get_object_or_404(Article.objects.published(), slug=slug)
	}
	return render(request, 'blog/detail.html', context)


def category(request, slug):
	context = {
		"category": get_object_or_404(Category, slug=slug, status=True)
	}

	return render(request, 'blog/category.html', context)