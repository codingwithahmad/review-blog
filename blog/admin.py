from django.contrib import admin
from .models import Article, Category
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "jpublish", "status", "category_to_str")
	list_filter = ("publish", "status")
	search_fields = ('title', 'slug')
	prepopulated_fields = {"slug": ("title",)}
	ordering = ['-status', '-publish']

	def category_to_str(self, obj):
		return ", ".join([category.title for category in obj.category.all()])

	category_to_str.short_description = "دسته بندی ها"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("position" ,"title", "slug", "status",)
	list_filter = (["status"])
	search_fields = ('title', 'slug')
	prepopulated_fields = {"slug": ("title",)}



