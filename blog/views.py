from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from .models import Article
# Create your views here.

def index(request):
	context = {
		"articles": Article.objects.filter(status="p").order_by("-publish")
	}
	return render(request, 'blog/home.html', context)

