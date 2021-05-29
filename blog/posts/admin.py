from django.contrib import admin
from .models import Post,UsersFollows
# Register your models here.

admin.site.register([Post,UsersFollows])