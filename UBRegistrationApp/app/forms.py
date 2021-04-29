"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import *

ADVISOR_MENU = [('View Students', 'View Students'), ('View Courses', 'View Courses'), 
                ('View/Send Messages', 'View/Send Messages'),
                ('View Login Information','View Login Information'), ('Change Login Information','Change Login Information')]

STUDENT_MENU = [('View Courses', 'View Courses'), ('View Enrolled Courses', 'View Enrolled Courses'), 
                ('Course Sign Up', 'Course Sign Up'),
                ('View/Send Messages', 'View/Send Messages'),
                ('View Login Information','View Login Information'), ('Change Login Information','Change Login Information')]

ADMIN_MENU = [('View Users', 'View Users'), ('Change User Information', 'Change User Information'), 
              ('View Courses', 'View Courses'), ('Change Courses', 'Change Courses'), ('View/Send Messages', 'View/Send Messages')]

CHANGE_MENU = [('Update', 'Update'), ('Add', 'Add')]

LOGIN_ROLES = [('Student', 'Student'), ('Advisor', 'Advisor'), ('Admin', 'Admin')]

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class LoginForm(forms.Form):
    inputUser = forms.CharField(label='Username', required=True)
    inputPass = forms.CharField(label='Password', required=True)
    role = forms.ChoiceField(label='Role', choices=LOGIN_ROLES, required=True)

class AdvisorMenuForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=ADVISOR_MENU, required=True)

class StudentMenuForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=STUDENT_MENU, required=True)

class AdminMenuForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=ADMIN_MENU, required=True)


class ChangeCoursesForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=CHANGE_MENU, required=True)
    courses = forms.ModelChoiceField(label='Courses', required=True, queryset=Section.objects.all())

class UpdateCourseForm(forms.Form):
    ProfName = forms.CharField(label='Professor Name', required=False)
    RoomNum = forms.CharField(label='Room Number', required=False)
    Credits = forms.IntegerField(label='Credits', required=False)
    Semester = forms.CharField(label='Semester', required=False)
    Seats = forms.IntegerField(label='Seats Left', required=False)

class AddCourseForm(forms.Form):
    DeptName = forms.CharField(label='Department Name', required=True)
    CourseName = forms.CharField(label='Course Name', required=True)
    SectionName = forms.CharField(label='Section Name', required=True)
    ProfName = forms.CharField(label='Professor Name', required=True)
    RoomNum = forms.CharField(label='Room Number', required=True)
    Credits = forms.IntegerField(label='Credits', required=True)
    Semester = forms.CharField(label='Semester', required=True)
    Seats = forms.IntegerField(label='Seats Left', required=True)

class EnrollCourseForm(forms.Form):
    courses = forms.ModelChoiceField(label='Courses', required=True, queryset=Section.objects.all())

class SendMessageForm(forms.Form):
    toUser = forms.ModelChoiceField(label='To: ', required=True, queryset=Login.objects.all())
    text = forms.CharField(label='Message', required=True)
    
# class ChangeLoginForm(forms.Form):
#     choice = forms.ChoiceField(label='Options Menu', choices=CHANGE_MENU, required=True)
#     courses = forms.ModelChoiceField(label='Courses', required=True, queryset=Section.objects.all())





