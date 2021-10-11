from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldMixin, FormValidMixin, AuthorAccessMixin
from django.views.generic import ListView, CreateView, UpdateView
from blog.models import Article
# Create your views here.


class ArticlesList(LoginRequiredMixin, ListView):
	template_name = "registration/home.html"	

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Article.objects.all()
		else:
			return Article.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FormValidMixin, FieldMixin, CreateView):
	model = Article
	fields = [ "author", "title", "slug", "category", "description", "thumbnail", "publish", "status",]
	template_name = "registration/article_create_update.html"	


class ArticleUpdate(AuthorAccessMixin, FormValidMixin, FieldMixin, UpdateView):
	model = Article
	fields = [ "author", "title", "slug", "category", "description", "thumbnail", "publish", "status",]
	template_name = "registration/article_create_update.html"	

	