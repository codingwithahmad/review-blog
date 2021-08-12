from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
	return HttpResponse("Hello")

def api(request):
	data = {
		"1": {
		"title": "مقاله اول",
		"id": 20,
		"slug": "first_article",
		},
		"2": {
		"title": "مقاله اول",
		"id": 20,
		"slug": "second_article",
		}
		,"3": {
		"title": "مقاله اول",
		"id": 20,
		"slug": "third_article",
		}
		,"4": {
		"title": "مقاله اول",
		"id": 20,
		"slug": "fourth_article",
		},
	}
	return JsonResponse(data)