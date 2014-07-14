from mezzanine import template
from mezzanine.utils.sites import current_site_id

from garis_theme.models import SitewideContent

register = template.Library()


@register.as_tag
def get_sitewide_content():
    """
    Adds the 'SitewideContent' to the context
    """
    return SitewideContent.objects.get_or_create(site_id=current_site_id())[0]



@register.filter(name='percentage_increase')
def percentage_increase(original, new):
    original = int(original)
    new = int(new)
    # Add new and old to get coorect differnce
    new = original + new

    increase =  new - original
    increase = (increase / original) * 100
    return abs(int(increase))
    
