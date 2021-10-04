from django.contrib import admin
from .models import Article, Category
# Register your models here.

#admin header change
admin.site.site_header = "وبلاگ جنگویی من"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ["title", "slug", "thumbnail_tag", "jpublish", "author", "status", "category_to_str"]
	list_filter = ("publish", "status", "author")
	search_fields = ('title', 'slug')
	prepopulated_fields = {"slug": ("title",)}
	ordering = ['-status', '-publish']
	actions = ['make_published', 'maek_draft']

	
	@admin.action(description="انتشار مقالات انتخاب شده")
	def make_published(self, request, queryset):
		row_updated = queryset.update(status="p")
		if row_updated == 1:
			message_bit = "منتشر شد."
		else:
			message_bit = "منشتر شدند."
		self.message_user(request, "{} مقاله {}".format(row_updated, message_bit))

	@admin.action(description="پیش نویس شدن مقالات انتخاب شده")
	def maek_draft(self, request, queryset):
		row_updated = queryset.update(status="d")
		if row_updated == 1:
			message_bit = "پیش نویس شد."
		else:
			message_bit = "پیش نویس شدند."
		self.message_user(request, "{} مقاله {}".format(row_updated, message_bit))

	

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("position" ,"title", "parent", "slug", "status",)
	list_filter = (["status"])
	search_fields = ('title', 'slug')
	prepopulated_fields = {"slug": ("title",)}



