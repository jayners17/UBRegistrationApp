CREATE TABLE College (
  Name varchar(20) NOT NULL UNIQUE,
  PRIMARY KEY (Name)
);
CREATE TABLE Login (
  ID_Number INT NOT NULL UNIQUE,
  Username varchar(20) NOT NULL UNIQUE,
  Password varchar(20) NOT NULL,
  PRIMARY KEY (ID_Number)
);
CREATE TABLE Advisor (
  ID_Number INT NOT NULL,
  Name varchar(20) NOT NULL,
  DName varchar(20) NOT NULL,
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES Login (ID_Number)
);
CREATE TABLE Department (
  DName varchar(20) NOT NULL UNIQUE,
  Name varchar(20) NOT NULL,
  Adv_ID_Num INT NOT NULL,
  PRIMARY KEY (DName),
  FOREIGN KEY (Name) REFERENCES College (Name),
  FOREIGN KEY (Adv_ID_Num) REFERENCES Advisor (ID_Number)
);
ALTER TABLE Advisor
ADD FOREIGN KEY (DName) REFERENCES Department (DName);
CREATE TABLE Course (
  CName varchar(20) NOT NULL UNIQUE,
  Room_Num varchar(20),
  Professor varchar(20) NOT NULL,
  Num_Credits INT NOT NULL,
  DName varchar(20) NOT NULL,
  PRIMARY KEY (CName),
  FOREIGN KEY (DName) REFERENCES Department (DName)
);
CREATE TABLE Section (
  CName varchar(20) NOT NULL,
  SName varchar(20) NOT NULL UNIQUE,
  Semester varchar(20) NOT NULL,
  Seats_Left INT NOT NULL,
  PRIMARY KEY (SName)
);
CREATE TABLE Student (
  ID_Number INT NOT NULL,
  Name varchar(20) NOT NULL,
  Adv_ID_Num INT NOT NULL,
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES Login (ID_Number),
  FOREIGN KEY (Adv_ID_Num) REFERENCES Advisor (ID_Number)
);
CREATE TABLE Admin (
  ID_Number INT NOT NULL,
  Name varchar(20) NOT NULL,
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES Login (ID_Number)
);
CREATE TABLE Enrolled (
  St_ID_Num INT NOT NULL,
  CName varchar(20) NOT NULL,
  SName varchar(20) NOT NULL,
  Current_Credits INT NOT NULL,
  FOREIGN KEY (St_ID_Num) REFERENCES Student (ID_Number),
  FOREIGN KEY (CName) REFERENCES Course (CName),
  FOREIGN KEY (SName) REFERENCES Section (SName)
);
CREATE TABLE Message (
  MEssage_Text TEXT,
  Time_Sent DATETIME,
  To_User varchar(20) NOT NULL,
  From_User varchar(20) NOT NULL,
  FOREIGN KEY (To_User) REFERENCES Login (Username),
  FOREIGN KEY (From_User) REFERENCES Login (Username)
);
CREATE TABLE Graduate (
  ID_Number INT NOT NULL,
  Degree_Program varchar(20),
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number)  REFERENCES Student (ID_Number)
);
CREATE TABLE Undergraduate (
  ID_Number INT NOT NULL,
  Class_Year INT,
  PRIMARY KEY (ID_Number),
  FOREIGN KEY (ID_Number) REFERENCES Student (ID_Number)
);
CREATE TABLE Majors (
  ID_Number INT NOT NULL,
  Major_Name varchar(20),
  PRIMARY KEY (Major_Name),
  FOREIGN KEY (ID_Number) REFERENCES Undergraduate (ID_Number)
);
CREATE TABLE Minors (
  ID_Number INT NOT NULL,
  Minor_Name varchar(20),
  PRIMARY KEY (Minor_Name),
  FOREIGN KEY (ID_Number) REFERENCES Undergraduate (ID_Number)
);
