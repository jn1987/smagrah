from django.db import models
from datetime import datetime

# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=256)
    body=models.TextField()
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "posts"

# Create your models here.
# class posts(models.Model):
#     title=models.CharField(max_length=256)
#     body=models.TextField()
#     created_at=models.DateTimeField(default=datetime.now,blank=True)
