from django.contrib import admin
from .models import BlogPost, Category, Comment


admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Comment)
