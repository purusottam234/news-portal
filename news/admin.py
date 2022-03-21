from django.contrib import admin

# Register your models here.

from .models import News,personDetails
admin.site.register(News)
admin.site.register(personDetails)
