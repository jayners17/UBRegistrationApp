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
from mysql.connector import connect, Error

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
                    print('student')
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

            if (option == 'View Students'):     #Done
                return redirect('/viewStudents/')
            elif (option == 'View Courses'): #Done
                return redirect('/viewCourses/')
            elif (option == 'View/Send Messages'): #Done
                return redirect('/messages/' + str(id) + '/')
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

            if (option == 'View Courses'):   #Done
                return redirect('/viewCourses/')
            elif (option == 'View Enrolled Courses'):
                print("") #need to add
            elif (option == 'Course Sign Up'):
                return redirect('/enrollCourse/' + str(id) + '/')
            elif (option == 'View/Send Messages'): #Done
                return redirect('/messages/' + str(id) + '/')
            elif (option == 'View Login Information'):
                print("") #need to add
            elif (option == 'Change Login Information'):
                print("") #need to add
    else:
        form = StudentMenuForm() # An unbound form
    return render(
        request,
        'app/student.html',
        {
            'title':'Student Page',
            'message':'',
            'year':datetime.now().year,
            'form': form,
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

            if (option == 'View Users'):    
                return redirect('')
            elif (option == 'Change User Information'):
                return redirect('')
            elif (option == 'View Courses'): #Done
                return redirect('/viewCourses/')
            elif (option == 'Change Courses'):
                return redirect('/changeCourses/')
            elif (option == 'View/Send Messages'): #Done
                return redirect('/messages/' + str(id) + '/')

    else:
        form = AdminMenuForm() # An unbound form
    return render(
        request,
        'app/admin1.html',
        {
            'title':'Admin Page',
            'message':'',
            'year':datetime.now().year,
            'form': form,
        }
    )

#Complete
def viewStudents(request):
    """Renders the viewStudents page."""
    assert isinstance(request, HttpRequest)

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            select_db_query = 'select DISTINCT Student.ID_Number, Student.Name, Advisor.Name, CASE '
            select_db_query+= 'WHEN Graduate.ID_Number = Student.ID_Number THEN Graduate.Degree_Program '
            select_db_query+= 'WHEN Undergraduate.ID_Number = Student.ID_Number THEN Undergraduate.Class_Year '
            select_db_query+= 'ELSE \'\' END AS ClassText, Major_Name '
            select_db_query+= 'from Advisor, Student, Majors, Undergraduate, Graduate '
            select_db_query+= 'where Advisor.ID_Number = Student.Adv_ID_Num AND (Undergraduate.ID_Number = Student.ID_Number OR Graduate.ID_Number = Student.ID_Number) AND Majors.ID_Number = Student.ID_Number '
            select_db_query+= 'Order By Student.ID_Number Asc'
            with connection.cursor() as cursor:
                cursor.execute(select_db_query)
                query_results = cursor.fetchall()
    except Error as e:
        print(e)

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

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('''Select Department.DName, Course.CName, SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left, College.Name
        From Course, Section, Department, College
        Where Section.CName = Course.CName AND Course.DName = Department.DName AND College.Name = Department.Name
        Order By Department.DName Asc, Course.CName Asc, SName Asc''')
                query_results = cursor.fetchall()
    except Error as e:
        print(e)

    return render(
        request,
        'app/viewCourses.html',
        {
            'title':'View Courses',
            'year':datetime.now().year,
            'query_results':query_results,
        }
    )

#Complete
def changeCourses(request):
    """Renders the changeCourses page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST': # If the form has been submitted...
        form = ChangeCoursesForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            option = form.cleaned_data['choice']
            course = form.cleaned_data['courses']

            if (option == 'Update'):   #Done
                return redirect('/updateCourse/' + str(course) + '/')
            elif (option == 'Delete'):
                print("") #need to add
            elif (option == 'Add'):
                return redirect('/addCourse/')
    else:
        form = ChangeCoursesForm() # An unbound form

    return render(
        request,
        'app/changeCourses.html',
        {
            'title':'Change Courses',
            'year':datetime.now().year,
            'form': form
        }
    )

#Complete
def updateCourse(request, sectionObj):
    """Renders the updateCourse page."""
    assert isinstance(request, HttpRequest)

    strA = sectionObj.split(": ")
    query = Section.objects.filter(cname=strA[0], sname=strA[1])

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            with connection.cursor() as cursor:
                stringA = 'Select Department.DName, Course.CName, SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left, College.Name '
                stringA += 'From Course, Section, Department, College Where Section.CName = Course.CName AND Course.DName = Department.DName AND College.Name = Department.Name AND Section.CName = \'' + str(query[0].cname) + '\' AND Section.SName = \'' + str(query[0].sname) + '\''
                print(stringA)
                cursor.execute(stringA)
                query_results = cursor.fetchall()
    except Error as e:
        print(e)

    for que in query_results:
        name = que[1]
        dept = que[0]
        secname = que[2]
        prof = que[3]
        room = que[4]
        credits = que[5]
        semest = que[6]
        seats = que[7]
        college = que[8]


    if request.method == 'POST': # If the form has been submitted...
        form = UpdateCourseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            if (form.cleaned_data['CourseName'] != ''):
                name = form.cleaned_data['CourseName']
            if (form.cleaned_data['SectionName'] != ''):
                secname = form.cleaned_data['SectionName']
            if (form.cleaned_data['ProfName'] != ''):
                prof = form.cleaned_data['ProfName']
            if (form.cleaned_data['RoomNum'] != ''):
                room = form.cleaned_data['RoomNum']
            if (form.cleaned_data['Credits'] != None):
                credits = form.cleaned_data['Credits']
            if (form.cleaned_data['Semester'] != ''):
                semest = form.cleaned_data['Semester']
            if (form.cleaned_data['Seats'] != None):
                seats = form.cleaned_data['Seats']

            
            try:
                with connect(
                    host="127.0.0.1",
                    user='root',
                    password='1234',
                    database='UBRegistrationDB',
                ) as connection:
                    with connection.cursor() as cursor:
                        stringE = 'UPDATE Enrolled SET '
                        stringS += 'Enrolled.CName = "%s", Enrolled.SName = "%s" ' % (name, secname)
                        stringS += 'WHERE Enrolled.CName = \'' + str(query[0].cname) + '\' AND Enrolled.SName = \'' + str(query[0].sname) + '\''
                        cursor.execute(stringE)
                        connection.commit()
                        print('enrolled')
                        stringC = 'UPDATE Course SET '
                        stringC += 'Course.CName = "%s", Course.Room_Num = "%s", Course.Professor = "%s", Course.Num_Credits = "%s" ' % (name, room, prof, str(credits))
                        stringC += 'WHERE Course.CName = \'' + str(query[0].cname) + '\''
                        cursor.execute(stringC)
                        connection.commit()
                        print('course')
                        stringS = 'UPDATE Section SET '
                        stringS += 'Section.CName = "%s", Section.SName = "%s", Section.Semester = "%s", Section.Seats_Left = "%s" ' % (name, secname, semest, str(seats))
                        stringS += 'WHERE Section.CName = \'' + str(query[0].cname) + '\' AND Section.SName = \'' + str(query[0].sname) + '\''
                        cursor.execute(stringS)
                        connection.commit()
                        print('section')
            except Error as e:
                print(e)
           
    else:
        form = UpdateCourseForm() # An unbound form

    return render(
        request,
        'app/updateCourse.html',
        {
            'title':'Update Course',
            'year':datetime.now().year,
            'form': form,
            'query_results': query_results
        }
    )

def addCourse(request):
    """Renders the addCourse page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST': # If the form has been submitted...
        form = AddCourseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            dept = form.cleaned_data['DeptName']
            name = form.cleaned_data['CourseName']
            secname = form.cleaned_data['SectionName']
            prof = form.cleaned_data['ProfName']
            room = form.cleaned_data['RoomNum']
            credits = form.cleaned_data['Credits']
            semest = form.cleaned_data['Semester']
            seats = form.cleaned_data['Seats']

            
            try:
                with connect(
                    host="127.0.0.1",
                    user='root',
                    password='1234',
                    database='UBRegistrationDB',
                ) as connection:
                    with connection.cursor() as cursor:
                        stringA = 'INSERT INTO Course (CName, Room_Num, Professor, Num_Credits, DName) VALUES ("%s", "%s", "%s", %d, "%s") ' % (name, room, prof, credits, dept)
                        cursor.execute(stringA)
                        connection.commit()
                        stringB = 'INSERT INTO Section (CName, SName, Semester, Seats_Left) VALUES ("%s", "%s", "%s", %d) ' % (name, secname, semest, seats)
                        cursor.execute(stringB)
                        connection.commit()
            except Error as e:
                print(e)
           
    else:
        form = AddCourseForm() # An unbound form

    return render(
        request,
        'app/addCourse.html',
        {
            'title':'Add A Course',
            'year':datetime.now().year,
            'form': form,
        }
    )

def enrollCourse(request, id):
    """Renders the enrollCourse page."""
    assert isinstance(request, HttpRequest)

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            with connection.cursor() as cursor:
                stringA = 'Select Department.DName, Course.CName, SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left, College.Name '
                stringA += 'From Course, Section, Department, College Where Section.CName = Course.CName AND Course.DName = Department.DName AND College.Name = Department.Name '
                cursor.execute(stringA)
                query_results = cursor.fetchall()
    except Error as e:
        print(e)


    if request.method == 'POST': # If the form has been submitted...
        form = EnrollCourseForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            course = form.cleaned_data['courses']

            query = Section.objects.filter(cname=course.cname, sname=course.sname)
            courseQ = Course.objects.filter(cname=course.cname)

            try:
                with connect(
                    host="127.0.0.1",
                    user='root',
                    password='1234',
                    database='UBRegistrationDB',
                ) as connection:
                    with connection.cursor() as cursor:
                        stringE = 'INSERT INTO Enrolled VALUES ("%s", "%s", "%s", "%s") ' % (id, query[0].cname, query[0].sname, courseQ[0].num_credits)
                        cursor.execute(stringE)
                        connection.commit()
            except Error as e:
                print(e)
           
    else:
        form = EnrollCourseForm() # An unbound form

    return render(
        request,
        'app/enrollCourse.html',
        {
            'title':'Enroll In A Course',
            'year':datetime.now().year,
            'form': form,
            'query_results': query_results
        }
    )

def messages(request, id):
    """Renders the messages page."""
    assert isinstance(request, HttpRequest)

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            with connection.cursor() as cursor:
                stringA = 'Select To_User, From_User, Time_Sent, Message_Text from Message, Login where Login.ID_Number = "%s" AND (To_User = Login.Username OR From_User = Login.Username)' % (str(id))
                cursor.execute(stringA)
                query_results = cursor.fetchall()
    except Error as e:
        print(e)


    if request.method == 'POST': # If the form has been submitted...
        form = SendMessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            to = form.cleaned_data['toUser']
            text = form.cleaned_data['text']
            date = datetime.now()
            login = Login.objects.filter(id_number = id)
            from1 = login[0].username

            try:
                with connect(
                    host="127.0.0.1",
                    user='root',
                    password='1234',
                    database='UBRegistrationDB',
                ) as connection:
                    with connection.cursor() as cursor:
                        stringE = 'INSERT INTO Message VALUES ("%s", "%s", "%s", "%s") ' % (text, date, to, from1)
                        cursor.execute(stringE)
                        connection.commit()
            except Error as e:
                print(e)
           
    else:
        form = SendMessageForm() # An unbound form

    return render(
        request,
        'app/messages.html',
        {
            'title':'View/Send Messages',
            'year':datetime.now().year,
            'form': form,
            'query_results': query_results
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

#incomplete
def viewLoginInfo(request):
    """Renders the viewLoginInfo page."""
    assert isinstance(request, HttpRequest)

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            with connection.cursor() as cursor:
                query = '''
                Select 
                From 
                Where 
                Order By
                '''
                cursor.execute(query)
                query_results = cursor.fetchall()
    except Error as e:
        print(e)

    return render(
        request,
        'app/viewLoginInfo.html',
        {
            'title':'View Login Info',
            'year':datetime.now().year,
            'query_results':query_results,
        }
    )

#incomplete
def viewEnrolledCourses(request, id):
    """Renders the viewEnrolledCourses page."""
    assert isinstance(request, HttpRequest)

    try:
        with connect(
            host="127.0.0.1",
            user='root',
            password='1234',
            database='UBRegistrationDB',
        ) as connection:
            with connection.cursor() as cursor:
                query = '''
                Select Course.CName, Course.SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left, DName, St_ID_Num
                From Course, Section, Enrolled
                Where St_ID_Num = id AND Course.CName = Enrolled.CName
                Order By Semester, CName, SName
                '''
                cursor.execute(query)
                query_results = cursor.fetchall()
    except Error as e:
        print(e)

    return render(
        request,
        'app/viewEnrolledCourses.html',
        {
            'title':'View Login Info',
            'year':datetime.now().year,
            'query_results':query_results,
        }
    )

