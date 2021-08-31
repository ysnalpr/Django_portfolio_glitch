from django.shortcuts import redirect, render
from django.contrib import messages

from .models import (Client, 
                Resume, 
                CodingSkill, 
                DesignSkill, 
                LanguageSkill, 
                Service, 
                Category, 
                Project)
from .forms import MessageForm


def home(request):
    return render(request, 'portfolio/home.html')

def resume(request):
    user = Resume.objects.get(id=request.user.id)
    design_skills = DesignSkill.objects.all()
    coding_skills = CodingSkill.objects.all()
    languages = LanguageSkill.objects.all()
    services = Service.objects.all()
    clients = Client.objects.all()
    return render(request, 'portfolio/resume.html', {'user': user,
        'coding_skills': coding_skills,
        'design_skills': design_skills,
        'languages': languages,
        'services': services,
        'clients': clients})

def portfolio(request):
    categories = Category.objects.all()
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'categories': categories})


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks, your message is sent successfully. We will contact you shortly!')
            return redirect('portfolio:contact')
    else:
        form = MessageForm()
    return render(request, 'portfolio/contact.html', {'form': form})