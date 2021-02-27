from django.contrib import admin
from . import models

admin.site.register(models.FilterType)
admin.site.register(models.Filter)
admin.site.register(models.Product)