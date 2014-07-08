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

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")

    def __str__(self):
        return self.heading

# class Paragraph(Orderable):
#     '''
#     A paragraph for paragraphs in HomePage
#     '''
#     homepage = models.ForeignKey(HomePage, related_name="slides")
#     text = models.TextField()
