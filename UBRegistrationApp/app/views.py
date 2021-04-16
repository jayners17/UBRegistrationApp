"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app import forms
from .forms import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            inUser = form.cleaned_data['inputUser']
            inPass = form.cleaned_data['inputPass']

    else:
        form = LoginForm() # An unbound form
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'form': form
        }
    )

def advisor(request):
    """Renders the advisor page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/advisor.html',
        {
            'title':'Advisor Page',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def student(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/student.html',
        {
            'title':'Student Page',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def admin1(request):
    """Renders the admin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/admin1.html',
        {
            'title':'Admin Page',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
