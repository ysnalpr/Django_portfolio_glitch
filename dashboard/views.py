from django.db.models import fields
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from portfolio.models import Client, DesignSkill, CodingSkill, LanguageSkill, Message, Service, Project, Category

def dash(request):
    if request.user.is_anonymous:
        raise Http404()
    services = Service.objects.all()
    clients = Client.objects.all()
    recent_projects = Project.objects.all().order_by('-id')[:3]
    return render(request, 'dashboard/dashboard.html', {'services': services, 'clients': clients, 'recent_projects': recent_projects})


# Design Skill
class DesignSkillCreate(LoginRequiredMixin, CreateView):
    model = DesignSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/designskill_form.html'


class DesignSkillUpdate(LoginRequiredMixin, UpdateView):
    model = DesignSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/designskill_form.html'


class DesignSkillDelete(LoginRequiredMixin, DeleteView):
    model = DesignSkill
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/designskill_confirm_delete.html'


# Coding Skill
class CodingSkillCreate(LoginRequiredMixin, CreateView):
    model = CodingSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/codingskill_form.html'


class CodingSkillUpdate(LoginRequiredMixin, UpdateView):
    model = CodingSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/codingskill_form.html'


class CodingSkillDelete(LoginRequiredMixin, DeleteView):
    model = CodingSkill
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/codingskill_confirm_delete.html'


# Language Skill
class LanguageSkillCreate(LoginRequiredMixin, CreateView):
    model = LanguageSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/languageskill_form.html'


class LanguageSkillUpdate(LoginRequiredMixin, UpdateView):
    model = LanguageSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/languageskill_form.html'


class LanguageSkillDelete(LoginRequiredMixin, DeleteView):
    model = LanguageSkill
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/skill/languageskill_confirm_delete.html'


def skills_list(request):
    if request.user.is_anonymous:
        raise Http404()
    
    design_skills = DesignSkill.objects.all()
    coding_skills = CodingSkill.objects.all()
    language_skills = LanguageSkill.objects.all()
    return render(request, 'dashboard/skill/skills_list.html', {'design_skills': design_skills, 'coding_skills': coding_skills, 'language_skills': language_skills})

def message_list(request):
    if request.user.is_anonymous:
        raise Http404()
    messages = Message.objects.all().order_by('is_read', '-created')
    return render(request, 'dashboard/message/message_list.html', {'messages': messages})


def message_detail(request, pk, name):
    if request.user.is_anonymous:
        raise Http404()
    message = get_object_or_404(Message, id=pk, name=name)
    message.is_read = True
    message.save()
    return render(request, 'dashboard/message/message_detail.html', {'message': message})


def services_clients_list(request):
    if request.user.is_anonymous:
        raise Http404()
    services = Service.objects.all()
    clients = Client.objects.all()
    return render(request, 'dashboard/services_clients/services_clients.html', {'services': services, 'clients': clients})

class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    fields = ['title', 'description', 'icon']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/services_clients/service_form.html'


class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    fields = ['title', 'description', 'icon']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/services_clients/service_form.html'


class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/services_clients/service_confirm_delete.html'


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['title', 'link', 'image']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/services_clients/client_form.html'


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['title', 'link', 'image']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/services_clients/client_form.html'


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/services_clients/client_confirm_delete.html'


def project_list(request):
    if request.user.is_anonymous:
        raise Http404()
    projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'dashboard/project/list.html', {'projects': projects, 'categories': categories})

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/project/category_form.html'


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/project/category_form.html'


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/project/category_confirm_delete.html'


class ProjectAdd(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/project/project_form.html'


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/project/project_form.html'


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('dashboard:project_list')
    template_name = 'dashboard/project/project_confirm_delete.html'