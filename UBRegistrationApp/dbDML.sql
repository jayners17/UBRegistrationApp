INSERT into College values 
('University of Bridgeport'),
('Sacred Heart University'),
('University of Connecticut');

INSERT into Login values
(000001,'Student1','Password1'),
(000002,'Student2','Password2'),
(000003,'Student3','Password3'),
(007001,'Advisor1','Password1'),
(007002,'Advisor2','Password2'),
(007003,'Advisor3','Password3'),
(700001,'Admin1','Password1'),
(700002,'Admin2','Password2'),
(700003,'Admin3','Password3');

INSERT into Advisor values
(007001,'Mr.Advisor1','CPSC'),
(007002,'Ms.Advisor2','MATH'),
(007003,'Dr.Advisor3','CPEG');

INSERT into Student values
(000001,'Romeo',007001),
(000002,'Jayne',007002),
(000003,'John',007003);

INSERT into Admin values
(700001,'Admin_A'),
(700002,'Admin_B'),
(700003,'Admin_C');

INSERT into Department values
('CPSC','University of Bridgeport',007001),
('MATH','Sacred Heart University',007002),
('CPEG','University of Connecticut',007003);

INSERT into Course values
('Advanced Database',301,'Professor Smith',3,'CPSC'),
('Prob & Stats',302,'Professor A',4,'MATH'),
('Physics I',303,'Professor Z',5,'CPEG');

INSERT into Section values
('Advanced Database','111A','Fall',10),
('Prob & Stats','HONORS-322','Fall',7),
('Physics I','513B','Spring',8);



INSERT into Enrolled values
(000001,'Advanced Database','111A',3),
(000002,'Prob & Stats','HONORS-322',4),
(000003,'Physics I','513B',5);

INSERT into Message values
("Hello",'2021-03-12 11:45:37','Advisor1','Student1'),
("Homework",'2021-04-24 15:09:51','Advisor2','Student2'),
("Exam",'2021-03-12 09:34:12','Advisor3','Student3');

INSERT into Graduate values
(000003,'PhD');

INSERT into Undergraduate values
(000001,'Junior'),
(000002,'Junior'),
(000003,'Junior');

INSERT into Majors values
(000001,'Computer Science'),
(000002,'Computer Science'),
(000003,'Math');

INSERT into Minors values
(000001,'Math'),
(000002,'Math');
