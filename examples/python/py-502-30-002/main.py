# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    actions = ['make_published']

    def make_published(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, f'{updated} записей опубликовано.')
    make_published.short_description = "Опубликовать выбранные записи"
