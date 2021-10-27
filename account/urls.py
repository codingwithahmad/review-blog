from django.urls import path
from django.contrib.auth import views
from .views import (
    ArticlesList, 
    ArticleCreate, 
    ArticleUpdate,
    ArticleDelete,
    Profile,
    
)


app_name = "account"



urlpatterns = [
    path('', ArticlesList.as_view(), name='home'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name='article-delete'),
    path('profile/', Profile.as_view(), name='profile'),
]