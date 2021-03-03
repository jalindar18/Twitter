from django.contrib import admin
from .models import tweettable, favtable

@admin.register(tweettable)
class AdminTweettable(admin.ModelAdmin):

    list_display = ['user','is_liked','created_date','modified_date']

admin.site.register(favtable)