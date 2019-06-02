from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):

    search_fields = ['message']

    list_filter = ['message']

    list_display = ['message', 'created_at']

admin.site.register(models.Post,PostAdmin)
