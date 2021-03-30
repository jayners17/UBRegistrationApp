CREATE TABLE Course (
  CName varchar(20),
  Room_Num INT(10),
  Professor varchar(20) NOT NULL UNIQUE,
  Num_Credits INT(10),
  DName varchar(20),
  PRIMARY KEY (CName),
  FOREIGN KEY (DName) REFERENCES DEPARTMENT (DName)
);
CREATE TABLE Section (
  CName varchar(20),
  SName varchar(20),
  Semester varchar(20),
  Seats_Left INT(10),
  PRIMARY KEY (SName),
  FOREIGN KEY (CName)
);
CREATE TABLE Department (
  DName varchar(20),
  Name varchar(20),
  Adv_ID_Num INT(10),
  PRIMARY KEY (DName),
  FOREIGN KEY (Name) REFERENCES COLLEGE (Name),
  FOREIGN KEY (Adv_ID_Num) REFERENCES ADVISOR (ID_Number)
);
CREATE TABLE College (
  Name varchar(20),
  PRIMARY KEY (Name)
);
CREATE TABLE Login (
  ID_Number INT(10),
  Username varchar(20) NOT NULL UNIQUE,
  Password varchar(20),
  PRIMARY KEY (ID_Number)
);
CREATE TABLE Advisor (
  ID_Number INT(10),
  Name varchar(20),
  DName varchar(20),
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES LOGIN (ID_Number),
  FOREIGN KEY (DName) REFERENCES DEPARTMENT (DName)
);
CREATE TABLE Student (
  ID_Number varchar(20),
  Name varchar(20),
  Adv_ID_Num INT(10),
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES LOGIN (ID_Number),
  FOREIGN KEY (Adv_ID_Num) REFERENCES ADVISOR (ID_Number)
);
CREATE TABLE Admin (
  ID_Number INT(10),
  Name varchar(20),
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES LOGIN (ID_Number)
);
CREATE TABLE Enrolled (
  St_ID_Num INT(10),
  CName varchar(20),
  SName varchar(20),
  Current_Credits INT(10),
  FOREIGN KEY (St_ID_Num) REFERENCES STUDENT (ID_Number),
  FOREIGN KEY (CName) REFERENCES SECTION (CName),
  FOREIGN KEY (SName) REFERENCES SECTION (SName)
);
CREATE TABLE Message (
  MEssage_Text TEXT,
  Time_Sent DATETIME,
  To_User varchar(20),
  From_User varchar(20),
  Adv_ID_Num INT(10),
  St_ID_Num INT(10),
  FOREIGN KEY (Adv_ID_Num) REFERENCES ADVISOR (Adv_ID_Num),
  FOREIGN KEY (St_ID_Num) REFERENCES STUDENT (ID_Number)
);
CREATE TABLE Graduate (
  ID_Number INT(10),
  Degree_Program varchar(20),
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number)  REFERENCES STUDENT (ID_Number)
);
CREATE TABLE Undergraduate (
  ID_Number varchar(20),
  Class_Year varchar(20),
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES STUDENT (ID_Number)
);
CREATE TABLE Majors (
  ID_Number INT(10),
  Major_Name varchar(20),
  PRIMARY KEY (Major_Name),
  FOREIGN KEY (ID_Number) REFERENCES UNDERGRADUATE (ID_Number)
);
CREATE TABLE Minors (
  ID_Number INT(10),
  Minor_Name varchar(20),
  PRIMARY KEY (Minor_Name),
  FOREIGN KEY (ID_Number) REFERENCES UNDERGRADUATE (ID_Number)
);
