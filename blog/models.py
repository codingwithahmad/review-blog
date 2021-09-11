from django.db import models
from django.utils import timezone
from extension.utils import jalali_convertor

# Create your models here.
class ArticleManager(models.Manager):

	def published(self):
		return self.filter(status="p")

class CategoryManager(models.Manager):

	def published(self):
		return self.filter(status=True)


class Category(models.Model):
	title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="جایگاه")
	class Meta:
		verbose_name = "دسته بندی"
		verbose_name_plural = "دسته بندی ها"
		ordering = ['position']

	def __str__(self):
		return self.title


	objects = CategoryManager()



class Article(models.Model):
	STATUS_CHOICES = (
			('d', 'پیش نویش'),
			('p', 'منتشر شده')
		)

	title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
	category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
	description = models.TextField(verbose_name="محتوا")
	thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
	publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now= True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

	class Meta:
		verbose_name = "مقاله"
		verbose_name_plural = "مقاله ها"
		ordering = ["-publish"]

	def __str__(self):
		return self.title

	def jpublish(self):
		return jalali_convertor(self.publish)

	jpublish.short_description = "زمان انتشار"


	objects = ArticleManager()