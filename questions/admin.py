from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Thread)
admin.site.register(models.Tag)
