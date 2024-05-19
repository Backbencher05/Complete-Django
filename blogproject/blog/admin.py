from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
    prepopulated_fields = {'slug': ('title',)}
    # To add filter on the admin portal 
    list_filter = ('status','author', 'created', 'publish')
    # To Add Search Option in the Admin Portal
    search_fields = ('title', 'body')
    # now it will come in search option, we can search using auther id 
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)