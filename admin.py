from django.contrib import admin

from .models import Spoiler, Title

class SpoilerInline(admin.TabularInline):
    model = Spoiler
    extra = 0

class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['title_text']}),
        ('Date information',  {'fields': ['sub_date'], 'classes': ['collapse']}),
    ]
    inlines = [SpoilerInline]

admin.site.register(Title, TitleAdmin)
