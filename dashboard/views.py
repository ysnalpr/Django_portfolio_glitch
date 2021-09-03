from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from portfolio.models import DesignSkill, CodingSkill, LanguageSkill

def dash(request):
    if request.user.is_anonymous:
        raise Http404()
    return render(request, 'dashboard/dashboard.html')


# Design Skill
class DesignSkillCreate(LoginRequiredMixin, CreateView):
    model = DesignSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/designskill_form.html'


class DesignSkillUpdate(LoginRequiredMixin, UpdateView):
    model = DesignSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/designskill_form.html'


class DesignSkillDelete(LoginRequiredMixin, DeleteView):
    model = DesignSkill
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/designskill_confirm_delete.html'


# Coding Skill
class CodingSkillCreate(LoginRequiredMixin, CreateView):
    model = CodingSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/codingskill_form.html'


class CodingSkillUpdate(LoginRequiredMixin, UpdateView):
    model = CodingSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/codingskill_form.html'


class CodingSkillDelete(LoginRequiredMixin, DeleteView):
    model = CodingSkill
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/codingskill_confirm_delete.html'


# Language Skill
class LanguageSkillCreate(LoginRequiredMixin, CreateView):
    model = LanguageSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/languageskill_form.html'


class LanguageSkillUpdate(LoginRequiredMixin, UpdateView):
    model = LanguageSkill
    fields = ['title', 'progress']
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/languageskill_form.html'


class LanguageSkillDelete(LoginRequiredMixin, DeleteView):
    model = LanguageSkill
    success_url = reverse_lazy('dashboard:dash')
    template_name = 'dashboard/languageskill_confirm_delete.html'


# TODO: Display all skills in skills page