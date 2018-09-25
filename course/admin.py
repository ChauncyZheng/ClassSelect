from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.CourseResource)
admin.site.register(models.CourseSelect)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.ConfirmString)
