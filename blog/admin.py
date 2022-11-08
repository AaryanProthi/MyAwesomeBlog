from django.contrib import admin
from .models import Post

admin.site.site_header = 'MyAwesomeBlog Admin'
admin.site.site_title = 'MyAwesomeBlog Admin Area'
admin.site.index_title = 'Welcome to the MyAwesomeBlog admin area'

admin.site.register(Post)