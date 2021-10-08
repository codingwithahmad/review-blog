from django.db import models
from account.models import User
from django.utils.html import format_html
from django.utils import timezone
from extension.utils import jalali_convertor
from django.urls import reverse

# Create your models here.
class ArticleManager(models.Manager):

	def published(self):
		return self.filter(status="p")

class CategoryManager(models.Manager):

	def published(self):
		return self.filter(status=True)


class Category(models.Model):
	parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,  related_name="children", verbose_name="زیردسته")
	title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
	slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
	status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
	position = models.IntegerField(verbose_name="جایگاه")
	class Meta:
		verbose_name = "دسته بندی"
		verbose_name_plural = "دسته بندی ها"
		ordering = ['parent__id', 'position']

	def __str__(self):
		return self.title


	objects = CategoryManager()



class Article(models.Model):
	STATUS_CHOICES = (
			('d', 'پیش نویش'),
			('p', 'منتشر شده')
		)

	author = models.ForeignKey(User, null=True,on_delete=models.SET_NULL, related_name="articles", verbose_name="نویسنده")
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

	def category_to_str(self):
		return ", ".join([category.title for category in self.category.published()])


	category_to_str.short_description = "دسته بندی ها"


	def thumbnail_tag(self):
		return format_html("<img width=100 height=75 style='border-radius: 10px' src='{}' />".format(self.thumbnail.url))

	thumbnail_tag.short_description = "نمایه"


	def get_absolute_url(self):
		return reverse("account:home")

	objects = ArticleManager()