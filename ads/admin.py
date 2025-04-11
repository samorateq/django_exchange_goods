from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ad, ExchangeProposal, Category


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "get_image")

    readonly_fields = ("get_image",)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="60"/>')
        return "-"

    get_image.short_description = "Изображение"

    
admin.site.register(ExchangeProposal)

admin.site.register(Category)