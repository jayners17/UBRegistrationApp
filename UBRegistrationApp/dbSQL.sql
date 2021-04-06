/* List of all courses and their information */
Create View Courses_List as
Select Department.DName, Course.CName, SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left, College.Name
From Course, Section, Department, College
Where Section.CName = Course.CName AND Course.DName = Department.DName AND College.Name = Department.Name
Order By Department.DName Asc, Course.CName Asc, SName Asc;

/* List all students who major in Computer Science */
Create View CPSC_Students as
Select Student.ID_Number, Student.Name, Student.Adv_ID_Num
From ((Student JOIN Undergraduate ON Student.ID_Number = Undergraduate.ID_Number) JOIN Majors ON Student.ID_Number = Majors.ID_Number)
Where Majors.Major_Name = "Computer Science"
Order By Student.Name Asc;

/* List all courses that are 3 credits */
Create View Three_Credit_Courses as
Select DName, CName
From Course
Where Num_Credits = 3
Order By DName Asc;

/* List all courses offered by the CPSC department */
Create View CPSC_Courses as
Select Course.CName, SName, Professor, Room_Num, Num_Credits, Semester, Seats_Left
From Course, Section
Where Section.CName = Course.CName AND Course.DName = "CPSC"
Order By Course.CName Asc, SName Asc;

/* List all the advisors with no students */
Create View Empty_Advisors as
Select ID_Number, Name, DName
From Advisor
Where Not Exists (Select * 
				  From Student
				  Where Advisor.Adv_ID_Num = Student.Adv_ID_Number);

/* List all courses taught by Ausif Mahmood */
Create View Mahmood_Courses as
Select DName, CName, Room_Num, Num_Credits
From Course
Where Professor = "Ausif Mahmood"
Order By DName Asc, CName Asc;                   