from django.urls import path
from .views import (
	ArticlesList,
	ArticleDetail,
	CategoryList,
	AuthorList,
	ArticlesPreview,
)

app_name="blog"
urlpatterns = [
	path('', ArticlesList.as_view(), name="index"),
	path('page/<int:page>', ArticlesList.as_view(), name="index"),
	path('detail/<slug:slug>', ArticleDetail.as_view(), name="detail"),
	path('preview/<int:pk>/', ArticlesPreview.as_view(), name="preview"),
	path('category/<slug:slug>', CategoryList.as_view(), name="category"),
	path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category"),
	path('author/<slug:username>', AuthorList.as_view(), name="author"),
	path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name="author")
]