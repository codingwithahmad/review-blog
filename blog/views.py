from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
	context = {
		"articles": [
			{
				"title": "پاسخ تند مجیدی به صحبتهای آقای ف!",
				"description": "فرهاد مجیدی ضمن اعلام مخالفت با فروش مهدی قایدی، از تلاش هایش برای اجاره کمپ تمرین، هتل مناسب و بازی دوستانه برای استقلال در امارات خبر داد.",
				"image": "https://static2.farakav.com/files/pictures/01633965.jpg",
			}
		]
	}
	return render(request, 'blog/home.html', context)

