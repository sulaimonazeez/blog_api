from django.db import models
from autoslug import AutoSlugField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title
    class Meta:
      ordering = ("-id",)