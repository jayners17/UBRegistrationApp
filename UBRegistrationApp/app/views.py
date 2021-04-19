"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app import forms
from .forms import *
from .models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            inUser = form.cleaned_data['inputUser']
            inPass = form.cleaned_data['inputPass']
            

            try:
                query = Login.objects.filter(Username = inUser, Password = inPass)
                id_num = query[0].ID_Number
            except:
                text = "Username and/or password are incorrect..."

            try:
                tryStudent = Student.objects.filter(ID_Number = id_num)
                return render(request,"app/student.html",{'id': id_num})
            except:
                print('Not a student')

            try:
                tryAdvisor = Advisor.objects.filter(ID_Number = id_num)
                return render(request,"app/advisor.html",{'id': id_num})
            except:
                print('Not an advisor')

            try:
                tryAdmin = Admin.objects.filter(ID_Number = id_num)
                return render(request,"app/admin1.html",{'id': id_num})
            except:
                print('Not an Admin')
            
    else:
        text = ""
        form = LoginForm() # An unbound form
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'message':'',
            'year':datetime.now().year,
            'form': form,
            'text': text,
        }
    )

def advisor(request):
    """Renders the advisor page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = AdvisorMenuForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            option = form.cleaned_data['choice']

            
            # redirect to page based on choice
    else:
        form = AdvisorMenuForm() # An unbound form
    return render(
        request,
        'app/advisor.html',
        {
            'title':'Advisor Page',
            'message':'',
            'year':datetime.now().year,
            'form': form
        }
    )

def student(request):
    """Renders the student page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = StudentMenuForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            option = form.cleaned_data['choice']

            
            # redirect to page based on choice
    else:
        form = StudentMenuForm() # An unbound form
    return render(
        request,
        'app/student.html',
        {
            'title':'Student Page',
            'message':'',
            'year':datetime.now().year,
        }
    )

def admin1(request):
    """Renders the admin page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = AdminMenuForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            option = form.cleaned_data['choice']

            
            # redirect to page based on choice
    else:
        form = AdminMenuForm() # An unbound form
    return render(
        request,
        'app/admin1.html',
        {
            'title':'Admin Page',
            'message':'',
            'year':datetime.now().year,
        }
    )

def viewStudents(request):
    """Renders the viewStudents page."""
    assert isinstance(request, HttpRequest)

    cursor = connection.cursor()
    cursor.execute('''select Student.ID_Number, Student.Name, Advisor.Name 
                    from Student, Advisor, Majors, Minors, Graduate, Undergraduate 
                    where Student.Adv_ID_Num = Advisor.ID_Number''')
    query_results = cursor.fetchall()

    return render(
        request,
        'app/viewStudents.html',
        {
            'title':'View Students',
            'year':datetime.now().year,
            'query_results':query_results,
        }
    )

def viewCourses(request):
    """Renders the viewCourses page."""
    assert isinstance(request, HttpRequest)
    query_results = Courses_List.objects.all()
    return render(
        request,
        'app/viewCourses.html',
        {
            'title':'View Courses',
            'year':datetime.now().year,
            'query_results':query_results,
        }
    )

def viewUsers(request):
    """Renders the viewUsers page."""
    assert isinstance(request, HttpRequest)
    query_results = Login.objects.all()
    return render(
        request,
        'app/viewCourses.html',
        {
            'title':'View Users',
            'year':datetime.now().year,
            'query_results':query_results,
        }
    )
