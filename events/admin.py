from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time',
                    'location', 'is_approved', 'owner')
    list_filter = ('is_approved', 'start_time')
    search_fields = ('title', 'description', 'location', 'owner__username')
    actions = ['approve_events', 'remove_approval']

    def approve_events(self, request, queryset):
        updated_count = queryset.update(is_approved=True)
        self.message_user(request, f"{updated_count} event(s) approved.")
    approve_events.short_description = "Approve selected events"

    def remove_approval(self, request, queryset):
        updated_count = queryset.update(is_approved=False)
        self.message_user(request, f"{updated_count} event(s) unapproved.")
    remove_approval.short_description = "Remove approval from selected events"
