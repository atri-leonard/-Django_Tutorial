from django.contrib import admin

from .models import Question
# Register your models here.

admin.site.register(Question)   #Register question model to admin in order to gain access to database