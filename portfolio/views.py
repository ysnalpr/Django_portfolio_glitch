from django.shortcuts import render
from .models import (Client, 
                Resume, 
                CodingSkill, 
                DesignSkill, 
                LanguageSkill, 
                Service, 
                Category, 
                Project)


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