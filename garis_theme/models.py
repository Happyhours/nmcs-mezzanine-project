from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged, SiteRelated
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
    '''
    A col-md-4 employee box
    '''
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


class ServicesPage(Page, RichText):
    '''
    A page representing the format of the services page
    '''
    heading = models.CharField(max_length=200,
        help_text="Heading for ServicesPage")
    subheading = models.CharField(max_length=200, blank=True,
        help_text="Optional subheading for ServicesPage")
    slider_heading = models.CharField(max_length=200, blank=True,
        help_text="Heading for slider")
    slider_text = models.TextField(blank=True,
        help_text="Optional text for slider")


    class Meta:
        verbose_name = _("Services page")
        verbose_name_plural = _("Services pages")

    def __str__(self):
        return self.heading


class Slide(Orderable):
    '''
    A slide in a slider connected to a ServicesPage
    '''
    servicespage = models.ForeignKey(ServicesPage)
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    link_to_image = models.CharField(max_length=2000, blank=True, default="#",
        help_text="Optional, if provided clicking the image will go here.")


class ServicesItem(Orderable):
    '''
    A col-md-4 mg-bt-40 services item box
    '''
    heading = models.CharField(max_length=50,
        help_text="Heading for service item")
    icon = models.CharField(max_length=50,
        help_text="Name of icon on service item")
    text = models.TextField(help_text="Text for service item")
    servicespage = models.ForeignKey(ServicesPage)

    def __str__(self):
        return self.heading


class ContactPage(Page, RichText):
    '''
    A page representing the format of the contact page
    '''
    heading = models.CharField(max_length=200,
        help_text="Heading for ContactPage")
    subheading = models.CharField(max_length=200, blank=True,
        help_text="Optional subheading for ContactPage")


    class Meta:
        verbose_name = _("Contact page")
        verbose_name_plural = _("Contact pages")

    def __str__(self):
        return self.heading


class ContactMap(Orderable):
    '''
    A model representing the map on the contact page
    '''
    latitude = models.CharField(max_length=50,
        help_text="Latitude")
    longitude = models.CharField(max_length=50,
        help_text="Longitude")
    address = models.TextField(help_text="Html text to be show when user clicks on map marker")
    color = models.CharField(max_length=50,
        help_text="Color")
    contactpage = models.ForeignKey(ContactPage)


class SitewideContent(SiteRelated):
    '''
    Represents the footer content
    '''
    box_one_title = models.CharField(max_length=200, default="Contact us")
    box_one_content = RichTextField()
    box_two_title = models.CharField(max_length=200, default="Sites we like")
    box_two_content = RichTextField()
    box_three_title = models.CharField(max_length=200, default="Highlighted pages")
    box_three_content = RichTextField()

    #box_four_title = models.CharField(max_length=200, default="Partners")

    class Meta:
        verbose_name = _('Sitewide Content')
        verbose_name_plural = _('Sitewide Content')


class PartnerImage(Orderable):
    '''
    A partner image in a slider connected to a SitewideContent
    '''
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.PartnerImage.image", "partner_image"),
        format="Image", max_length=255, null=True, blank=True)
    link_to_image = models.CharField(max_length=2000, blank=True, default="#",
        help_text="Optional, if provided clicking the image will go here.")
    sitewidecontent = models.ForeignKey(SitewideContent)


class OpenTimeData(Orderable):
    '''
    Data for table in SiteWideContent
    '''
    text = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    sitewidecontent = models.ForeignKey(SitewideContent)  

    def __str__(self):
        return self.text + " " + self.time


class OpenTimeAlert(Orderable):
    '''
    An alert that represents important text "Closed 28 juli" connected to a SitewideContent
    '''
    text = RichTextField()
    sitewidecontent = models.ForeignKey(SitewideContent) 

    def __str__(self):
        return self.text


class FooterContactData(Orderable):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    icon = models.CharField(max_length=20)
    sitewidecontent = models.ForeignKey(SitewideContent) 

    def __str__(self):
        return self.title


class PortfolioPage(Page, RichText):
    '''
    A collection of individual portfolio items
    '''
    heading = models.CharField(max_length=200,
        help_text="Heading for HomePage")
    subheading = models.CharField(max_length=200, blank=True,
        help_text="Optional subheading for HomePage")

    class Meta:
        verbose_name = _("Portfolio page")
        verbose_name_plural = _("Portfolios pages")


class PortfolioItem(Orderable):
    '''
    A portfolio item
    '''
    job = models.TextField(help_text="Information about job")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("garis_theme.PortfolioItem.image", "portfolio_item"),
        format="Image", max_length=255, null=True, blank=True)
    before_power = models.CharField(max_length=50)
    after_power = models.CharField(max_length=50)
    portfoliopage = models.ForeignKey(PortfolioPage)



