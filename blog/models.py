from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.TextField()
	thumbnail = models.ImageField(upload_to="images")
	publish = models.DateTimeField(default=timezone.now)
