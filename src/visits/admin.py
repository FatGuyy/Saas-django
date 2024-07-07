from django.contrib import admin
from visits.models import PageVisit

@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'path')


