from django import template
from ..models import Social

register = template.Library()

@register.inclusion_tag('portfolio/partials/footer.html')
def social_media():
    socials = Social.objects.all()
    return {'socials': socials}