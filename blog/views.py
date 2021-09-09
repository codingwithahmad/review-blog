from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Article, Category
# Create your views here.

def index(request):
	context = {
		"articles": Article.objects.filter(status="p"),
	}
	return render(request, 'blog/home.html', context)


def detail(request, slug):
	context = {
		"art": get_object_or_404(Article, slug=slug, status="p")
	}
	return render(request, 'blog/detail.html', context)