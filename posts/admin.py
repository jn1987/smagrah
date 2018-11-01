from django.contrib import admin

# Register your models here.
from .models import posts
# admin.site.register(posts)
# list_display = ('Title', 'Body')

class postsAdmin(admin.ModelAdmin):
      admin.site.register(posts)
      fields = ('title', 'body')

class AuthorAdmin(admin.ModelAdmin):
 
      exclude = ('slug',)