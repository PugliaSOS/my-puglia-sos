from django.contrib import admin
from poll.models import Poll, Submitting

class PollAdmin(admin.ModelAdmin):
    fields = ['name', 'html']
    list_display = ['name']

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(PollAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PollAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

admin.site.register(Poll, PollAdmin)
