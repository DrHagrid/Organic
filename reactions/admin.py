from django.contrib import admin
from .models import *


class ReactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reaction._meta.fields]

    class Meta:
        model = Reaction


class ReceivingReactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ReceivingReaction._meta.fields]

    class Meta:
        model = ReceivingReaction


admin.site.register(Reaction, ReactionAdmin)
admin.site.register(ReceivingReaction, ReceivingReactionAdmin)
