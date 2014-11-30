from django.contrib import admin
from event.models import Event, Meeting, EventAttachment

class MeetingInline(admin.StackedInline):
    fieldsets = [
        (
            None,
            {'fields': ['title', 'datetime']}
        ),
        (
            'Extra informations',
            {'fields': ['description'], 'classes': ['collapse']}
        )
        ]
    model = Meeting

class EventAttachmentInline(admin.StackedInline):
    model = EventAttachment

class EventAdmin(admin.ModelAdmin):
    inlines = [MeetingInline, EventAttachmentInline]

admin.site.register(Event, EventAdmin)
