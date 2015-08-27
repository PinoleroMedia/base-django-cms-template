from django.contrib import admin
from django.utils.translation import gettext as _
from apps.content.models import *


class SectionImageInline(admin.TabularInline):
    model = SectionImage
    extra = 2
    verbose_name = _('Carousel')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', )
    inlines = [SectionImageInline, ]
    readonly_fields = ('name',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
	 list_display = ('title', )
	 readonly_fields = ('title', )