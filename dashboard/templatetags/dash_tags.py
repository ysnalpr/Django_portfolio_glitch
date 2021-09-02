from django import template
from portfolio.models import Message, Client, Project, CodingSkill, DesignSkill, LanguageSkill

register = template.Library()

@register.inclusion_tag('dashboard/partials/message_templatetags.html')
def show_latest_messages(count=4):
    latest_messages = Message.objects.filter(is_read=False).order_by('-created')[:count]
    return {'latest_messages': latest_messages}

@register.inclusion_tag('dashboard/partials/skill_templatetags.html')
def design_skills(count=4):
    skills = DesignSkill.objects.all()
    return {'skills': skills, 'title': 'Design Skills'}

@register.inclusion_tag('dashboard/partials/skill_templatetags.html')
def coding_skills(count=4):
    skills = CodingSkill.objects.all()
    return {'skills': skills, 'title': 'Coding Skills'}

@register.inclusion_tag('dashboard/partials/skill_templatetags.html')
def language_skills(count=4):
    skills = LanguageSkill.objects.all()
    return {'skills': skills, 'title': 'Language Skills'}

@register.simple_tag
def clients_count():
    return Client.objects.all().count()

@register.simple_tag
def projects_count():
    return Project.objects.all().count()

@register.simple_tag
def unread_messages_count():
    return Message.objects.filter(is_read=False).count()

@register.simple_tag
def read_messages_count():
    return Message.objects.filter(is_read=True).count()
