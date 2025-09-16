from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'rating',
                    'created_at', 'updated_at')
    list_filter = ('created_at', 'owner__username', 'rating', )
    search_fields = ('owner__username', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    actions = ['delete_selected_reviews']
