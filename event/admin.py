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
    fields = ['title', 'description']
    list_display = ['title', 'owner']
    inlines = [MeetingInline, EventAttachmentInline]

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(EventAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

admin.site.register(Event, EventAdmin)
