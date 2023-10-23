from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    ('draft','Borrador'),
    ('posted','Publicado')
)

class Post(models.Model):
    # To create post in website

    title = models.CharField(
        max_length=300
    )

    slug = models.SlugField(
        max_length=200, 
        unique=True
    )

    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    content = models.TextField(
    )

    status = models.CharField(
        choices=STATUS, 
        default='draft'
    )

    updated_on = models.DateTimeField(
        auto_now= True
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-created_on']

    def __str__(self):
        return self.title


