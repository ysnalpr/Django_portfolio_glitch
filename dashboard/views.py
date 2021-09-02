from django.http.response import Http404
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