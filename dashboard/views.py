from django.http.response import Http404
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required


# @login_required
def dash(request):
    if request.user.is_anonymous:
        raise Http404()
    return render(request, 'dashboard/dashboard.html')