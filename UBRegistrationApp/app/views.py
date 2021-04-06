"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
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
