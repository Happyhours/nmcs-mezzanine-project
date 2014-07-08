from django.contrib import admin

# Register your models here.
from garis_theme.models import (
    HomePage,
)

# class HomePageAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,  {'fields': ['heading','subheading']}),
#         #('jallo',  {'fields': ['comment']}),
#     ]

# admin.site.register(HomePage, HomePageAdmin)



from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin



class HomePageAdmin(PageAdmin):
    pass


admin.site.register(HomePage, HomePageAdmin)