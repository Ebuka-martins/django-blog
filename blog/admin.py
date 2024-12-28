# from django.contrib import admin
# from .models import Post

# # Register your models here.
# admin.site.register(Post)
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)

