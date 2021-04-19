from django.db import models


class Admin(models.Model):
    id_number = models.OneToOneField('Login', models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Admin'


class Advisor(models.Model):
    id_number = models.OneToOneField('Login', models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    dname = models.ForeignKey('Department', models.DO_NOTHING, db_column='DName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Advisor'


class College(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'College'


class Course(models.Model):
    cname = models.CharField(db_column='CName', primary_key=True, max_length=50)  # Field name made lowercase.
    room_num = models.CharField(db_column='Room_Num', max_length=50, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=50)  # Field name made lowercase.
    num_credits = models.IntegerField(db_column='Num_Credits')  # Field name made lowercase.
    dname = models.ForeignKey('Department', models.DO_NOTHING, db_column='DName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Course'


class Department(models.Model):
    dname = models.CharField(db_column='DName', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.ForeignKey(College, models.DO_NOTHING, db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Department'


class Enrolled(models.Model):
    st_id_num = models.ForeignKey('Student', models.DO_NOTHING, db_column='St_ID_Num')  # Field name made lowercase.
    cname = models.ForeignKey(Course, models.DO_NOTHING, db_column='CName')  # Field name made lowercase.
    sname = models.ForeignKey('Section', models.DO_NOTHING, db_column='SName')  # Field name made lowercase.
    current_credits = models.IntegerField(db_column='Current_Credits')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enrolled'


class Graduate(models.Model):
    id_number = models.OneToOneField('Student', models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    degree_program = models.CharField(db_column='Degree_Program', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Graduate'


class Login(models.Model):
    id_number = models.IntegerField(db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login'


class Majors(models.Model):
    id_number = models.OneToOneField('Undergraduate', models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    major_name = models.CharField(db_column='Major_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Majors'


class Message(models.Model):
    message_text = models.TextField(db_column='Message_Text', blank=True, null=True)  # Field name made lowercase.
    time_sent = models.DateTimeField(db_column='Time_Sent', blank=True, null=True)  # Field name made lowercase.
    to_user = models.ForeignKey(Login, models.DO_NOTHING, db_column='To_User',related_name='message_to')  # Field name made lowercase.
    from_user = models.ForeignKey(Login, models.DO_NOTHING, db_column='From_User',related_name='message_from')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Message'


class Minors(models.Model):
    id_number = models.OneToOneField('Undergraduate', models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    minor_name = models.CharField(db_column='Minor_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minors'


class Section(models.Model):
    cname = models.CharField(db_column='CName', max_length=50)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', primary_key=True, max_length=50)  # Field name made lowercase.
    semester = models.CharField(db_column='Semester', max_length=50)  # Field name made lowercase.
    seats_left = models.IntegerField(db_column='Seats_Left')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Section'


class Student(models.Model):
    id_number = models.OneToOneField(Login, models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    adv_id_num = models.ForeignKey(Advisor, models.DO_NOTHING, db_column='Adv_ID_Num')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'


class Undergraduate(models.Model):
    id_number = models.OneToOneField(Student, models.DO_NOTHING, db_column='ID_Number', primary_key=True)  # Field name made lowercase.
    class_year = models.CharField(db_column='Class_Year', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Undergraduate'
