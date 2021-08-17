from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "publish", "status",)
	list_filter = ("publish", "status")
	search_fields = ('title', 'slug')
	prepopulated_fields = {"slug": ("title",)}
	ordering = ['-status', '-publish']



