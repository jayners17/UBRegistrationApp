"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

ADVISOR_MENU = [('View Students', 'View Students'), ('View Courses', 'View Courses'), 
                ('View Messages', 'View Messages'), ('Send Message', 'Send Message'),
                ('View Login Information','View Login Information'), ('Change Login Information','Change Login Information')]

STUDENT_MENU = [('View Courses', 'View Courses'), ('View Enrolled Courses', 'View Enrolled Courses'), 
                ('Course Sign Up', 'Course Sign Up'),
                ('View Messages', 'View Messages'), ('Send Message', 'Send Message'),
                ('View Login Information','View Login Information'), ('Change Login Information','Change Login Information')]

ADMIN_MENU = [('View Users', 'View Users'), ('Change User Information', 'Change User Information'), 
              ('View Courses', 'View Courses'), ('Change Courses', 'Change Courses'), 
                ('View Messages', 'View Messages')]

CHANGE_MENU = [('Update', 'Update'), ('Delete', 'Delete'), ('Add', 'Add')]

LOGIN_MENU = [('Student', 'Student'), ('Advisor', 'Advisor'), ('Admin', 'Admin')]

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
    role = forms.ChoiceField(label='Role', choices=LOGIN_MENU, required=True)

class AdvisorMenuForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=ADVISOR_MENU, required=True)

class StudentMenuForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=STUDENT_MENU, required=True)

class AdminMenuForm(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=ADMIN_MENU, required=True)

class ChangeTable(forms.Form):
    choice = forms.ChoiceField(label='Options Menu', choices=CHANGE_MENU, required=True)