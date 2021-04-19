"""
Definition of urls for UBRegistrationApp.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('advisor/<id>/', views.advisor, name='advisor'),
    path('student/<id>/', views.student, name='student'),
    path('admin1/<id>/', views.admin1, name='admin1'),
    path('viewStudents/', views.viewStudents, name='viewStudents'),
    path('viewCourses/', views.viewCourses, name='viewCourses'),
    path('viewUsers/', views.viewUsers, name='viewUsers'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
]
