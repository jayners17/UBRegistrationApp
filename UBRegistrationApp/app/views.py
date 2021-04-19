"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect
from app import forms
from .forms import *
from app import models
from .models import *

#complete
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            inUser = form.cleaned_data['inputUser']
            inPass = form.cleaned_data['inputPass']
            inRole = form.cleaned_data['role']


            try:
                query = Login.objects.filter(username = inUser, password = inPass)
                id_num = query[0].id_number

            except:
                text = "Username and/or password are incorrect..."

            if (inRole == "Student"):
                try:
                    tryS = Student.objects.filter(id_number = id_num)
                    return redirect('/student/'+ str(id_num) + '/')
                except:
                    text = "Role is incorrect..."
            elif (inRole == 'Advisor'):
                try:
                    tryA = Advisor.objects.filter(id_number = id_num)
                    return redirect('/advisor/'+ str(id_num) + '/')
                except:
                    text = "Role is incorrect..."
            elif (inRole == 'Admin'):
                try:
                    tryAd = Admin.objects.filter(id_number = id_num)
                    return redirect('/admin1/'+ str(id_num) + '/')
                except:
                    text = "Role is incorrect..."
                
            
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

def advisor(request, id):
    """Renders the advisor page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST': # If the form has been submitted...
        form = AdvisorMenuForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            option = form.cleaned_data['choice']

            if (option == 'View Students'):
                return render(request,"app/viewStudents.html",{}) #Not Done
            elif (option == 'View Courses'):
                return render(request,"app/viewCourses.html",{}) #Done
            elif (option == 'View Messages'):
                print("") #need to add
            elif (option == 'Send Message'):
                print("") #need to add
            elif (option == 'View Login Information'):
                print("") #need to add
            elif (option == 'Change Login Information'):
                print("") #need to add
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

def student(request, id):
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

def admin1(request, id):
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


#Complete
def viewCourses(request):
    """Renders the viewCourses page."""
    assert isinstance(request, HttpRequest)
    
    cursor = connection.cursor()
    cursor.execute('''Select Department.DName, Course.CName, SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left, College.Name
        From Course, Section, Department, College
        Where Section.CName = Course.CName AND Course.DName = Department.DName AND College.Name = Department.Name
        Order By Department.DName Asc, Course.CName Asc, SName Asc''')
    query_results = cursor.fetchall()

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
