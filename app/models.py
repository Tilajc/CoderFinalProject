from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=15)
    version= models.FloatField()
    subtitle= models.CharField(max_length=30)
    body= models.TextField(max_length=300)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    img= models.ImageField(upload_to="posts_img")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    message= models.TextField(max_length=500)
    date= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.author}: {self.message}'
