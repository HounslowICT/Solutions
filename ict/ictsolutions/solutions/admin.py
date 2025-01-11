from django.contrib import admin
from .models import Solution


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('slug', 'solution', 'clase', 'date', 'link')  # Add fields you want to display

admin.site.register(Solution, SolutionAdmin)