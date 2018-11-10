from django.contrib import admin
from . import models


class GroupMemeberInline(admin.TabularInline):
    model = models.GroupMember

# Register your models here.
admin.site.register(models.Group)