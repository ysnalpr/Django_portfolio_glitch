from django.contrib import admin
from .models import (Resume,
                CodingSkill, 
                DesignSkill, 
                LanguageSkill, 
                Service, 
                Client, 
                Category, 
                Project, 
                Social, 
                Message)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'job']
    list_editable = ['age', 'email']


@admin.register(DesignSkill)
class DesignSkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'progress']
    list_editable = ['progress']


@admin.register(CodingSkill)
class CodingSkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'progress']
    list_editable = ['progress']

@admin.register(LanguageSkill)
class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'progress']
    list_editable = ['progress']


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'link']
    list_editable = ['category']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read']
    list_editable = ['is_read']