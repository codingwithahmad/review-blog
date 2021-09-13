from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
	path('', views.index, name="index"),
	path('page/<int:page>', views.index, name="index"),
	path('detail/<slug:slug>', views.detail, name="detail"),
	path('category/<slug:slug>', views.category, name="category"),
	path('category/<slug:slug>/page/<int:page>', views.category, name="category")
]