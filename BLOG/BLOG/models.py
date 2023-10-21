from django.db import models

class BlogPost(models.Model):
    blog_name = models.CharField(max_length=255)
    blog_image = models.ImageField(upload_to="blog_images/")
    blog_description = models.TextField()


