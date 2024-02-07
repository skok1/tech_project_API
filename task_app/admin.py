from django.contrib import admin
from .models import Task, Category


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'end_at', 'completed')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('completed',)
    list_filter = ('completed', 'created_at', 'updated_at',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Category, CategoryAdmin)
