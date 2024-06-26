from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length =225)
    author = models.ForeignKey(User,related_name ='blog_posts',on_delete=models.CASCADE)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created= models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length= 10, choices=STATUS_CHOICES,default= 'draft')
    objects = CustomManager()
    class Meta:
        # when we use query post.object.all() it will come in order 
        # we don't need to use order by
        ordering = ('-publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug ])