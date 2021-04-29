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
    path('viewLoginInfo/<id>/', views.viewLoginInfo, name='viewLoginInfo'),
    path('changeCourses/', views.changeCourses, name='changeCourses'),
    path('updateCourse/<sectionObj>/', views.updateCourse, name='updateCourse'),
    path('enrollCourse/<id>/', views.enrollCourse, name='enrollCourse'),
    path('viewEnrolledCourses/<id>/', views.viewEnrolledCourses, name='viewEnrolledCourses'),
    path('addCourse/', views.addCourse, name='addCourse'),
    path('messages/<id>/', views.messages, name='messages'),
    path('changeLoginInfo/', views.changeLoginInfo, name='changeLoginInfo'),

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
