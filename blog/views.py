from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
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
	paginate_by = 1

# def detail(request, slug):
# 	context = {
# 		"art": get_object_or_404(Article.objects.published(), slug=slug)
# 	}
# 	return render(request, 'blog/detail.html', context)

class ArticleDetail(DetailView):
	
	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404(Article.objects.published(), slug=slug)


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