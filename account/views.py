from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
	FieldMixin, 

	FormValidMixin, 

	AuthorAccessMixin, 

	SuperUserAccessMixin
)
from django.views.generic import (

	ListView, 

	CreateView, 

	UpdateView,

	DeleteView,
)
from blog.models import Article
from .models import User
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


class ArticleDelete(SuperUserAccessMixin, DeleteView):
	model = Article
	success_url = reverse_lazy('account:home')
	template_name = 'registration/article_confirm_delete.html'

	
class Profile(UpdateView):
	model = User
	template_name = "registration/profile.html"
	fields = ['username', 'email', 'first_name', 'last_name',
	 'special_user', 'is_author']

	success_url = reverse_lazy("account:profile")

	def get_object(self):
		return User.objects.get(pk = self.request.user.pk)


