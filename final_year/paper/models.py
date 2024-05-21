from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    
    def __str__(self) -> str:
        return self.name

class vlog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=300)
    publication_date = models.IntegerField()
    author = models.CharField( max_length=300)
    
    def __str__(self) -> str:
        return self.title
