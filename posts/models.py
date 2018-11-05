from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib import admin

# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=250,blank=True)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "posts"

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while posts.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class PostAdmin(admin.ModelAdmin):
      list_display = ('Title', 'Body')


# Create your models here.
# class posts(models.Model):
#     title=models.CharField(max_length=256)
#     body=models.TextField()
#     created_at=models.DateTimeField(default=datetime.now,blank=True)
