from django.contrib import admin
from django.db.utils.translation import gettext as _
from apps.content.model import *


class SectionImageInline(admin.TabularInLine):
    model = SectionImage
    extra = 2
    verbose_name = _('Carousel')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', )
    inlines = [SectionImageInline, ]
    readonly_fields = ('name',)
