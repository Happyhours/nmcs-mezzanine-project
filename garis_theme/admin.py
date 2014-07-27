from django.contrib import admin

from mezzanine.core.admin import SingletonAdmin

# Register your models here.
from garis_theme.models import (
    HomePage,
    AboutPage,
    Employee,
    ServicesPage,
    Slide,
    ServicesItem,
    ContactPage,
    ContactMap,
    SitewideContent,
    PartnerImage,
    OpenTimeData,
    OpenTimeAlert,
    FooterContactData,
    PortfolioPage,
    PortfolioItem,
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


class EmployeeInline(TabularDynamicInlineAdmin):
    model = Employee
    extra = 1
    fieldsets = (None, {
        "fields": ["name", "position", "text", "image", "_order"],
    }),


class AboutPageAdmin(PageAdmin):
    inlines = [EmployeeInline]


admin.site.register(AboutPage, AboutPageAdmin)


class SlideItemInline(TabularDynamicInlineAdmin):
    model = Slide
    extra = 3


class ServicesItemInline(TabularDynamicInlineAdmin):
    model = ServicesItem
    extra = 3


class ServicesPageAdmin(PageAdmin):
    inlines = [SlideItemInline, ServicesItemInline]


admin.site.register(ServicesPage, ServicesPageAdmin)


class ContactMapInline(TabularDynamicInlineAdmin):
    model = ContactMap


class ContactPageAdmin(PageAdmin):
    inlines = [ContactMapInline]


admin.site.register(ContactPage, ContactPageAdmin)


class PartnerImageInline(TabularDynamicInlineAdmin):
    model = PartnerImage


class OpenTimeDataInline(TabularDynamicInlineAdmin):
    model = OpenTimeData


class OpenTimeAlertInline(TabularDynamicInlineAdmin):
    model = OpenTimeAlert


class FooterContactDataInline(TabularDynamicInlineAdmin):
    model = FooterContactData


class SitewideContentAdmin(SingletonAdmin):
    inlines = [PartnerImageInline, OpenTimeDataInline, OpenTimeAlertInline, FooterContactDataInline]


admin.site.register(SitewideContent, SitewideContentAdmin)


class PortfolioItemInline(TabularDynamicInlineAdmin):
    model = PortfolioItem


class PortfolioPageAdmin(PageAdmin):
    inlines = [PortfolioItemInline]


admin.site.register(PortfolioPage, PortfolioPageAdmin)

# from copy import deepcopy
# from mezzanine.galleries.admin import GalleryAdmin
# from mezzanine.galleries.models import Gallery, GalleryImage


# m_fieldsets = deepcopy(GalleryAdmin.fieldsets)

# #m_fieldsets[0][1]["fields"].insert(-1, "sold") // THIS LINE CAUSE ERROR

# class MyGalleryAdmin(GalleryAdmin):
#     fieldsets = m_fieldsets

# admin.site.unregister(Gallery)
# admin.site.register(Gallery, MyGalleryAdmin)

