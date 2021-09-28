from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
	path('', views.ArticlesList.as_view(), name="index"),
	path('page/<int:page>', views.ArticlesList.as_view(), name="index"),
	path('detail/<slug:slug>', views.ArticleDetail.as_view(), name="detail"),
	path('category/<slug:slug>', views.CategoryList.as_view(), name="category"),
	path('category/<slug:slug>/page/<int:page>', views.CategoryList.as_view(), name="category"),
	path('author/<slug:username>', views.AuthorList.as_view(), name="author"),
	path('author/<slug:username>/page/<int:page>', views.AuthorList.as_view(), name="author")
]