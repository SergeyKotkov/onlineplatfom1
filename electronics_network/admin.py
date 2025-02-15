from django.contrib import admin
from .models import NetworkNode

class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city')
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = 'Clear debt'

admin.site.register(NetworkNode, NetworkNodeAdmin)