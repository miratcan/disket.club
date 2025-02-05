from django.contrib import admin
from .models import Disket

class DisketAdmin(admin.ModelAdmin):
    list_display = ('label', 'author', 'created_at')
    search_fields = ('label', 'content')
    list_filter = ('visibility', 'approved', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Disket, DisketAdmin)
