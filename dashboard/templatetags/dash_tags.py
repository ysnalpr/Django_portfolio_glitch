from django import template
from portfolio.models import Message

register = template.Library()

@register.inclusion_tag('dashboard/partials/message_templatetags.html')
def show_latest_messages(count=4):
    latest_messages = Message.objects.order_by('-created')[:count]
    return {'latest_messages': latest_messages}