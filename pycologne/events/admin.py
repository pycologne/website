from django.contrib import admin

from . import models


class ParticipantInline(admin.StackedInline):
	model = models.Participant


admin.site.register(models.Location,
    list_display=("title", "slug", "city", "link"),
    list_filter=("city",)
)

admin.site.register(models.Event,
    list_display=('date', 'title', 'location', 'kind'),
    list_filter=('location','kind'),
    inlines=(ParticipantInline,),
)
