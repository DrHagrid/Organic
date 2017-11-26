from django.contrib import admin
from reactions.models import *


class ReactionInline(admin.TabularInline):
    model = Reaction
    extra = 0


class ReceivingReactionInline(admin.TabularInline):
    model = ReceivingReaction
    extra = 0


class OrganicClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrganicClass._meta.fields]
    inlines = [ReactionInline, ReceivingReactionInline]

    class Meta:
        model = OrganicClass


admin.site.register(OrganicClass, OrganicClassAdmin)
