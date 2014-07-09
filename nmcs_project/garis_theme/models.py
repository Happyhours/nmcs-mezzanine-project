from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

# Create your models here.


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="Heading for HomePage")
    subheading = models.CharField(max_length=200, blank=True,
        help_text="Optional subheading for HomePage")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.HomePage.image", "feature_image"),
        format="Image", max_length=255, null=True, blank=True)
    link_to_image = models.CharField(max_length=2000, blank=True, default="#",
        help_text="Optional, if provided clicking the image will go here.")


    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")

    def __str__(self):
        return self.heading


class AboutPage(Page, RichText):
    '''
    A page representing the format of the about page
    '''
    heading = models.CharField(max_length=200,
        help_text="Heading for AboutPage")
    subheading = models.CharField(max_length=200, blank=True,
        help_text="Optional subheading for AboutPage")


    class Meta:
        verbose_name = _("About page")
        verbose_name_plural = _("About pages")

    def __str__(self):
        return self.heading


class Employee(Orderable):
    name = models.CharField(max_length=50,
        help_text="Employee name")
    position = models.CharField(max_length=100, blank=True,
        help_text="Employee position")
    text = models.TextField(help_text="Information about employee")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.AboutPage.image", "employee_image"),
        format="Image", max_length=255)
    aboutpage = models.ForeignKey(AboutPage)

    def __str__(self):
        return self.name