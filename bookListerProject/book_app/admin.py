# user: ubuntu
# password: admin123

from django.contrib import admin
from .models import Book

# register models here
admin.site.register(Book)