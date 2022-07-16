from django.contrib import admin

from first_form.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp')
