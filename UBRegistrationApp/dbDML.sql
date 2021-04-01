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
(007001,'Mr.Advisor1','Department_X'),
(007002,'Ms.Advisor2','Department_Y'),
(007003,'Dr.Advisor3','Department_Z');

INSERT into Department values
('Department_X','University of Bridgeport',007001),
('Department_Y','Sacred Heart University',007002),
('Department_Z','University of Connecticut',007003);

INSERT into Course values
('Advanced Database',301,'Professor_X',3,'Department_X'),
('Prob & Stats',302,'Professor_Y',4,'Department_Y'),
('Physics I',303,'Professor_Z',5,'Department_Z');

INSERT into Section values
('Advanced Database','Computer Science','Fall',10),
('Prob & Stats','Math','Fall',7),
('Physics I','Physics','Spring',8);

INSERT into Student values
(000001,'Romeo',007001),
(000002,'Jayne',007002),
(000003,'John',007003);

INSERT into Admin values
(700001,'Admin_A'),
(700002,'Admin_B'),
(700003,'Admin_C');

INSERT into Enrolled values
(000001,'Advanced Database','Computer Science',3),
(000002,'Prob & Stats','Math',4),
(000003,'Physics I','Physics',5);

INSERT into Message values
("Hello",2021-03-12 11:45:37,'Advisor1','Student1'),
("Homework",2021-04-24 15:09:51,'Advisor2','Student2'),
("Exam",2021-03-12 09:34:12,'Advisor3','Student3');

INSERT into Graduate values
(000003,'PhD');

INSERT into Undergraduate values
(000001,'Junior'),
(000002,'Junior')

INSERT into Majors values
(000001,'Computer Science'),
(000002,'Computer Science');

INSERT into Minors values
(000001,'Math'),
(000002,'Math');
