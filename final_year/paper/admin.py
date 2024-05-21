from django.contrib import admin

# Register your models here.
from .models import Author,vlog
admin.site.register(Author)
admin.site.register(vlog)
