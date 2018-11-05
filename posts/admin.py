from django.contrib import admin

# Register your models here.
from .models import posts
# admin.site.register(posts)
# list_display = ('Title', 'Body')

class postsAdmin(admin.ModelAdmin):
      admin.site.register(posts)
      fields = ('title', 'body')

class postsAdmin(admin.ModelAdmin):
 
      exclude = ('slug',)