from django.contrib import admin

# Register your models here.
from garis_theme.models import (
    HomePage,
)

class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['heading','subheading']}),
        #('jallo',  {'fields': ['comment']}),
    ]

admin.site.register(HomePage, HomePageAdmin)