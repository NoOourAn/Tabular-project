import prettytable as prettytable
from random import randint
from random import random
from datetime import datetime

class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self): return self._id

    def get_name(self): return self._name

    def __str__(self): return self._name


class Student:
    def __init__(self, id, name, courses):
        self._id = id
        self._name = name
        self._courses = courses

    def get_id(self): return self._id

    def get_name(self): return self._name

    def get_courses(self): return self._courses

    def __str__(self): return self._name


# class StudentCategory:
#     def __init__(self, courses, students):
#         self._courses = courses
#         self._students = students
#
#     def get_courses(self): return self._courses
#     def get_students(self): return self._students
class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity

    def get_number(self): return self._number

    def get_seatingCapacity(self): return self._seatingCapacity


class TimeAvilable:
    def __init__(self, id, time, day, date):
        self.id = id
        self.time = time
        self.day = day
        self.date = date

    def get_id(self): return self.id

    def get_time(self): return self.time

    def get_day(self): return self.day

    def get_date(self): return self.date



class Courses:
    def __init__(self, number, name, instructors, students, maxNumbOfStudents):  # maxnumber htb2a len(students)
        self._number = number
        self._name = name
        self._instructors = instructors
        self._students = students
        self.maxNumbOfStudents = maxNumbOfStudents

    def get_number(self): return self._number

    def get_name(self): return self._name

    def get_instructors(self): return self._instructors

    def get_students(self): return self._students

    def get_maxNumbOfStudents(self): return self.maxNumbOfStudents

    def __str__(self): return self._name


class Department:
    def __init__(self, name, Courses):
        self._name = name
        self._Courses = Courses

    def get_name(self): return self._name

    def get_Courses(self): return self._Courses


class Data:
    ROOMS = [["R1", 350], ["R2", 350], ["R3", 350], ["R4", 350], ["R5", 350], ["R6", 350], ["R7", 350], ["R8", 350],
             ["R9", 350], ["R10", 350]]  # excelsheet
    Time_Avilable = [[1, "09:00 - 10:00", "SUNDAY" , "1/1"],
                     [2, "10:00 - 11:00", "SUNDAY" , "1/1"],
                     [3 , "11:00 - 12:00", "SUNDAY" , "1/1"],
                     [4 , "09:00 - 10:00", "SUNDAY" , "8/1"],
                     [5 , "10:00 - 11:00", "SUNDAY" , "8/1"],
                     [6 , "11:00 - 12:00", "SUNDAY" , "8/1"],
                     [7 , "09:00 - 10:00", "SUNDAY" , "15/1"],
                     [8 , "10:00 - 11:00", "SUNDAY" , "15/1"],
                     [9 , "11:00 - 12:00", "SUNDAY" , "15/1"],
                     [10 , "09:00 - 10:00", "SUNDAY" , "22/1"],
                     [11 , "10:00 - 11:00", "SUNDAY" , "22/1"],
                     [12 , "11:00 - 12:00", "SUNDAY" , "22/1"],
                     [13 , "09:00 - 10:00", "MONDAY" , "2/1"],
                     [14 , "10:00 - 11:00", "MONDAY" , "2/1"],
                     [15 , "11:00 - 12:00", "MONDAY" , "2/1"],
                     [16 , "09:00 - 10:00", "MONDAY" , "9/1"],
                     [17 , "10:00 - 11:00", "MONDAY" , "9/1"],
                     [18 , "11:00 - 12:00", "MONDAY" , "9/1"],
                     [19 , "09:00 - 10:00", "MONDAY" , "16/1"],
                     [20 , "10:00 - 11:00", "MONDAY" , "16/1"],
                     [21 , "11:00 - 12:00", "MONDAY" , "16/1"],
                     [22 , "09:00 - 10:00", "MONDAY" , "23/1"],
                     [23 , "10:00 - 11:00", "MONDAY" , "23/1"],
                     [24 , "11:00 - 12:00", "MONDAY" , "23/1"],
                     [25 , "09:00 - 10:00", "TUESDAY" , "3/1"],
                     [26 , "10:00 - 11:00", "TUESDAY" , "3/1"],
                     [27 , "11:00 - 12:00", "TUESDAY" , "3/1"],
                     [28 , "09:00 - 10:00", "TUESDAY" , "10/1"],
                     [29 , "10:00 - 11:00", "TUESDAY" , "10/1"],
                     [30 , "11:00 - 12:00", "TUESDAY" , "10/1"],
                     [31 , "09:00 - 10:00", "TUESDAY" , "17/1"],
                     [32 , "10:00 - 11:00", "TUESDAY" , "17/1"],
                     [33 , "11:00 - 12:00", "TUESDAY" , "17/1"],
                     [34 , "09:00 - 10:00", "TUESDAY" , "24/1"],
                     [35 , "10:00 - 11:00", "TUESDAY" , "24/1"],
                     [36 , "11:00 - 12:00", "TUESDAY" , "24/1"],
                     [37 , "09:00 - 10:00", "WEDNSDAY" , "4/1"],
                     [38 , "10:00 - 11:00", "WEDNSDAY" , "4/1"],
                     [39 , "11:00 - 12:00", "WEDNSDAY" , "4/1"],
                     [40 , "09:00 - 10:00", "WEDNSDAY" , "11/1"],
                     [41 , "10:00 - 11:00", "WEDNSDAY" , "11/1"],
                     [42 , "11:00 - 12:00", "WEDNSDAY" , "11/1"],
                     [43 , "09:00 - 10:00", "WEDNSDAY" , "18/1"],
                     [44 , "10:00 - 11:00", "WEDNSDAY" , "18/1"],
                     [45 , "11:00 - 12:00", "WEDNSDAY" , "18/1"],
                     [46 , "09:00 - 10:00", "WEDNSDAY" , "25/1"],
                     [47 , "10:00 - 11:00", "WEDNSDAY" , "25/1"],
                     [48 , "11:00 - 12:00", "WEDNSDAY" , "25/1"],
                     [49 , "09:00 - 10:00", "THURSDAY" , "5/1"],
                     [50 , "10:00 - 11:00", "THURSDAY" , "5/1"],
                     [51 , "11:00 - 12:00", "THURSDAY" , "5/1"],
                     [52 , "09:00 - 10:00", "THURSDAY" , "12/1"],
                     [53 , "10:00 - 11:00", "THURSDAY" , "12/1"],
                     [54 , "11:00 - 12:00", "THURSDAY" , "12/1"],
                     [55 , "09:00 - 10:00", "THURSDAY" , "19/1"],
                     [56 , "10:00 - 11:00", "THURSDAY" , "19/1"],
                     [57 , "11:00 - 12:00", "THURSDAY" , "19/1"],
                     [58 , "09:00 - 10:00", "THURSDAY" , "26/1"],
                     [59 , "10:00 - 11:00", "THURSDAY" , "26/1"],
                     [60 , "11:00 - 12:00", "THURSDAY" , "26/1"]]
    INSTRUCTORS = [["id-1", "DR Gean"],
                   ["id-2", "DR James"],
                   ["id-3", "Mr Mike"],
                   ["id-4", "DR Steve"]]
    STUDENT = [["id-1", "nour", "mm ir"],
               ["id-2", "kera", "mm ir"],
               ["id-3", "simba", "ds logic"],
               ["id-4", "Limo", "or pat"],
               ["id-5", "neer", "ds logic"],
               ["id-6", "shimngi", "pl logic"]]

    # cat = {"mm":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'] ,
    #        "ai":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'],
    #        "co":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'],
    #        "os2":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'],
    #        "concepts":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'],
    #        "ethics":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'],
    #        "db2":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'],
    #        "ir":['Jabbaar', 'el-Abdul', 'Patrick', 'Carnes', 'Shawn', 'O', 'Bryan', 'Jenna', 'Whitney', 'Kaitlin', 'Krueger', 'Jaime', 'Mikesell', 'Katelynn', 'Andrie', 'Maryn', 'Manzanares', 'Colleen', 'Kohout', 'Daniel', 'Spurlin', 'Trevor', 'Bulba', 'Jordan', 'Burkhamer', 'Rebecca', 'Ah', 'Fat', 'Christopher', 'Jacobo', 'Min', 'Singal', 'Corey', 'Rademacher', 'Alexander', 'Reed', 'Dalen', 'Whiting', 'Chelsea', 'Persky', 'Karla', 'Taylor', 'Kaden', 'Yates', 'Maimoona', 'el-Soliman', 'Aaqil', 'el-Hashemi', 'Sean', 'Bruso', 'Andrew', 'Bishop', 'Zahraaa', 'el-Yousef', 'Surya', 'Ky', 'George', 'Mann', 'Latino', 'Calderon', 'Baylen', 'Cloutier', 'Nicole', 'Torres', 'Valadez', 'Addie', 'Villa', 'vicencio', 'Billy', 'Jack', 'Bestle', 'Isabella', 'Martinez', 'Kimberly', 'Thielke', 'Adrian', 'Miguel', 'Gomez', 'Kayla', 'Sales', 'Haafiza', 'al-Attar', 'Juanita', 'Medina', 'Emma', 'Kim', 'Mckayla', 'Dopler', 'Jonathan', 'Nevarez', 'Roger', 'Redfern', 'Hannah', 'Critchfield', 'Chue', 'Fue', 'Richter', 'Joshua', 'Mesan', 'Dylan', 'Bell', 'Troy','Brandilyn', 'Hanselman', 'Nicole', 'Patria', 'Kyler', 'Grieshaber', 'Jasper', 'Stang', 'Anthony', 'Visocsky', 'Jake', 'Seime', 'Dasha',   'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller', 'Terri', 'John', 'Ferry', 'Michelle', 'Goldanloo', 'Ryan', 'Heidebrecht', 'Murtidevi', 'Chung', 'Arely', 'Rodriguez', 'Taylor', 'Stone', 'Melody',  'Michaela', 'Schoenbeck', 'Charles', 'Prose', 'Brittany', 'Kemmerzell', 'Taryn', 'Springfield', 'Matthew', 'Obourn', 'Travis', 'Poss', 'Brittany', 'Fernandez','Mulvahill', 'Eliana', 'Michelsen', 'Dane', 'Whittemore'] ,
    #        "logic":[ 'Lindsey', 'Carter', 'Duncan', 'Kruse', 'Callahan', 'Foster', 'Jamie', 'Ortiz', 'Ryan', 'Barrett', 'Samuel', 'Palmer', 'Riley', 'Mcloughlin', 'Aimee', 'Apelyan', 'Maryah', 'Falloon', 'Lucille', 'Mitchell', 'Christian', 'Zambrano', 'Munoz', 'Bryce', 'Vaillancourt', 'Brandilyn', 'Collins', 'Konner', 'Gearhart', 'Andrew', 'Houghton', 'Marisa', 'Ramey', 'Magdalynne', 'Noah', 'Megan', 'Salamena', 'Meghan', 'Arnold', 'James', 'Rice', 'Wesley', 'Nunn', 'Gareth', 'Newkirk', 'Austin', 'Harline', 'Courtney', 'Martinez', 'Alexandra', 'Graham', 'Alexander', 'Swearingen', 'Brandy', 'Waldner', 'Coleman', 'Keelen', 'Casey', 'Buhr', 'Shauna', 'Sneed', 'Caitlin', 'Dean', 'Andrew', 'Kirin', 'Nadia', 'Minks', 'Ivy', 'Lucero', 'Kevin', 'Curry', 'Charles', 'Cramer', 'Emily', 'Warner', 'Mckenzie', 'Haycock', 'Faviola', 'Soto', 'Stephen', 'Wharton', 'Alexandria', 'Fortner', 'Savannah', 'Kivett', 'Tanner', 'Jones', 'Luisa', 'Bautista', 'Juhaina', 'al-Bilal', 'Siena', 'Ingram', 'Alondra', 'Gardea', 'Corral', 'Vincent', 'Webster', 'Abdul', 'Felipe', 'Martinez', 'Acosta', 'Emma', 'Casias', 'Adolf', 'Malik', 'Christian', 'Chow', 'Asad', 'el-Yacoub', 'Holly', 'Marshall',  'Veronica', 'Tounzen', 'Haley', 'Ingrim', 'Hyrup', 'Kayla', 'Sandefur', 'Rylee', 'Onstott', 'Kelli', 'Bartolome', 'Thomas', 'Chanlynn', 'Hannah', 'Ratterman', 'Alexandria', 'Winter', 'Ryan', 'Russell', 'Logan', 'Nighswonger', 'Zaghlool', 'al-Pasha', 'Madeline', 'Kremke','Jesse', 'Carballo', 'Robert', 'Podolski', 'Viridiana', 'Ballesteros', 'Michael', 'Griffin', 'Chad', 'Klemp', 'Weldon', 'Hightower', 'Daniel', 'Pierce', 'Austin', 'Haas', 'Madison', 'Fithian', 'Zachary'] ,
    #        "or":[ 'Lindsey', 'Carter', 'Duncan', 'Kruse', 'Callahan', 'Foster', 'Jamie', 'Ortiz', 'Ryan', 'Barrett', 'Samuel', 'Palmer', 'Riley', 'Mcloughlin', 'Aimee', 'Apelyan', 'Maryah', 'Falloon', 'Lucille', 'Mitchell', 'Christian', 'Zambrano', 'Munoz', 'Bryce', 'Vaillancourt', 'Brandilyn', 'Collins', 'Konner', 'Gearhart', 'Andrew', 'Houghton', 'Marisa', 'Ramey', 'Magdalynne', 'Noah', 'Megan', 'Salamena', 'Meghan', 'Arnold', 'James', 'Rice', 'Wesley', 'Nunn', 'Gareth', 'Newkirk', 'Austin', 'Harline', 'Courtney', 'Martinez', 'Alexandra', 'Graham', 'Alexander', 'Swearingen', 'Brandy', 'Waldner', 'Coleman', 'Keelen', 'Casey', 'Buhr', 'Shauna', 'Sneed', 'Caitlin', 'Dean', 'Andrew', 'Kirin', 'Nadia', 'Minks', 'Ivy', 'Lucero', 'Kevin', 'Curry', 'Charles', 'Cramer', 'Emily', 'Warner', 'Mckenzie', 'Haycock', 'Faviola', 'Soto', 'Stephen', 'Wharton', 'Alexandria', 'Fortner', 'Savannah', 'Kivett', 'Tanner', 'Jones', 'Luisa', 'Bautista', 'Juhaina', 'al-Bilal', 'Siena', 'Ingram', 'Alondra', 'Gardea', 'Corral', 'Vincent', 'Webster', 'Abdul', 'Felipe', 'Martinez', 'Acosta', 'Emma', 'Casias', 'Adolf', 'Malik', 'Christian', 'Chow', 'Asad', 'el-Yacoub', 'Holly', 'Marshall',  'Veronica', 'Tounzen', 'Haley', 'Ingrim', 'Hyrup', 'Kayla', 'Sandefur', 'Rylee', 'Onstott', 'Kelli', 'Bartolome', 'Thomas', 'Chanlynn', 'Hannah', 'Ratterman', 'Alexandria', 'Winter', 'Ryan', 'Russell', 'Logan', 'Nighswonger', 'Zaghlool', 'al-Pasha', 'Madeline', 'Kremke','Jesse', 'Carballo', 'Robert', 'Podolski', 'Viridiana', 'Ballesteros', 'Michael', 'Griffin', 'Chad', 'Klemp', 'Weldon', 'Hightower', 'Daniel', 'Pierce', 'Austin', 'Haas', 'Madison', 'Fithian', 'Zachary'],
    #        "pat": [ 'Lindsey', 'Carter', 'Duncan', 'Kruse', 'Callahan', 'Foster', 'Jamie', 'Ortiz', 'Ryan', 'Barrett', 'Samuel', 'Palmer', 'Riley', 'Mcloughlin', 'Aimee', 'Apelyan', 'Maryah', 'Falloon', 'Lucille', 'Mitchell', 'Christian', 'Zambrano', 'Munoz', 'Bryce', 'Vaillancourt', 'Brandilyn', 'Collins', 'Konner', 'Gearhart', 'Andrew', 'Houghton', 'Marisa', 'Ramey', 'Magdalynne', 'Noah', 'Megan', 'Salamena', 'Meghan', 'Arnold', 'James', 'Rice', 'Wesley', 'Nunn', 'Gareth', 'Newkirk', 'Austin', 'Harline', 'Courtney', 'Martinez', 'Alexandra', 'Graham', 'Alexander', 'Swearingen', 'Brandy', 'Waldner', 'Coleman', 'Keelen', 'Casey', 'Buhr', 'Shauna', 'Sneed', 'Caitlin', 'Dean', 'Andrew', 'Kirin', 'Nadia', 'Minks', 'Ivy', 'Lucero', 'Kevin', 'Curry', 'Charles', 'Cramer', 'Emily', 'Warner', 'Mckenzie', 'Haycock', 'Faviola', 'Soto', 'Stephen', 'Wharton', 'Alexandria', 'Fortner', 'Savannah', 'Kivett', 'Tanner', 'Jones', 'Luisa', 'Bautista', 'Juhaina', 'al-Bilal', 'Siena', 'Ingram', 'Alondra', 'Gardea', 'Corral', 'Vincent', 'Webster', 'Abdul', 'Felipe', 'Martinez', 'Acosta', 'Emma', 'Casias', 'Adolf', 'Malik', 'Christian', 'Chow', 'Asad', 'el-Yacoub', 'Holly', 'Marshall',  'Veronica', 'Tounzen', 'Haley', 'Ingrim', 'Hyrup', 'Kayla', 'Sandefur', 'Rylee', 'Onstott', 'Kelli', 'Bartolome', 'Thomas', 'Chanlynn', 'Hannah', 'Ratterman', 'Alexandria', 'Winter', 'Ryan', 'Russell', 'Logan', 'Nighswonger', 'Zaghlool', 'al-Pasha', 'Madeline', 'Kremke','Jesse', 'Carballo', 'Robert', 'Podolski', 'Viridiana', 'Ballesteros', 'Michael', 'Griffin', 'Chad', 'Klemp', 'Weldon', 'Hightower', 'Daniel', 'Pierce', 'Austin', 'Haas', 'Madison', 'Fithian', 'Zachary'],
    #        "cs":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'],
    #        "is":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'],
    #        "math1":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'],
    #        "eng1":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'],
    #        "phy":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'],
    #        "elec":['Natasha', 'Yarusso', 'Brooke', 'Cazares', 'Rochelle', 'Johnson', 'Joey', 'Abreu', 'Preston', 'Suarez', 'Lee', 'Dong', 'Maaiz', 'al-Dia', 'Maja', 'Nicholson', 'Sasha', 'Jansen', 'Edgar', 'Sanchez', 'Kolbi', 'Strunk', 'Brittany', 'Sath', 'Meggan', 'Smith', 'Ericka', 'ArreolaDavid', 'Pulc', 'Kyle', 'Luckey', 'Rojesh', 'Her', 'David', 'Weber', 'Rachel', 'Jambor', 'Musab', 'al-Moustafa', 'Sila', 'Nguyen', 'Samantha', 'Hicks', 'Angela', 'Harding', 'Brandon', 'Barbour', 'Reilly', 'Wagar', 'Victoria', 'Ibarra', 'Dakota', 'Wirth', 'Lauren', 'Klocker', 'Michael', 'Benson', 'Sean', 'Rozga', 'Cody', 'Vermeylen', 'Kinaana', 'al-Jamail', 'Daniel', 'Garcia', 'Katrina', 'Saito', 'Joshua', 'Galloway', 'Aylin', 'Mendoza', 'Sharon', 'Fyfe', 'Afnaan', 'el-Mohammed', 'Jesse', 'Williams', 'Kenny', 'Fukushima', 'Tawnie', 'Glaisher', 'Britany', 'Stevens', 'Alan', 'Trinh', 'Zoe', 'Kern', 'Sidney', 'Beavers', 'Miriam', 'Aguilar', 'Issac', 'Mata', 'Hannah', 'Uren', 'Zachary', 'Bradley', 'Moira', 'Buttitto', 'Nicole', 'Humpal', 'Georgia','White', 'Sabaaha', 'al-Latif', 'Grant', 'Walden', 'Kitty', 'Nguyen', 'Tyler', 'Kibel', 'Kyler', 'Overboe', 'Alexander', 'Lizama', 'Bannock', 'Lee', 'Anthony', 'Mcdevitt', 'Darby', 'Focken', 'Abigail', 'Gallegos', 'Patricia', 'Rockhold', 'Kylie', 'Schafer', 'Katherine', 'Andrew', 'Yelich', 'Dimitri', 'Castillo', 'Matthew', 'Strasburger', 'Vittoria', 'Faulkner', 'Tyler', 'Goetz', 'Tyler', 'Weller','Bowyer', 'Bryant', 'Ronquillo', 'Garrett', 'Heim', 'Cody', 'Amen', 'Jasmine', 'Lopez', 'William', 'Tierney', 'Matthew', 'Sputh', 'Brenna', 'Chapman', 'Blake','Cody', 'Smith', 'Nicolas', 'Papp', 'Christopher'],
    #        "econ":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "it":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "math2":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "stat":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "eng2":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "pl":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "algo":['Williams', 'Connor', 'Ferry', 'Amanda', 'Tatum', 'Cameron', 'Steinberg', 'Shuraih', 'el-Karim', 'Katelyn', 'Sharp', 'Colin', 'Lemont', 'Donald', 'Nevins', 'Macaela', 'Kadillak', 'Brittany', 'Pratt', 'Cameron', 'Hancock', 'William', 'Grevious', 'Lindsey', 'Job', 'Gabrielle', 'Smith', 'Allison', 'Brink', 'Lomme', 'Sheyenne', 'Delgado', 'Manzanares', 'Joseph', 'Smith', 'Fikra', 'al-Mina', 'Aurelia', 'Davis', 'Ingham', 'Taylor', 'Elstun', 'Joseph', 'Snider', 'Sourinthone', 'Tran', 'Ibrahim', 'al-Sawaya', 'Alexandra', 'Levy', 'Macie', 'Nguyen', 'Sean', 'Tegtman', 'Casey', 'Vanden', 'Bos', 'Staci', 'Maes', 'Luke', 'Davey', 'Harper', 'Wheeler-Marques', 'Sherleen', 'Saravanan', 'Myles', 'Vaught', 'Juan', 'Guerrero', 'Camacho', 'Lindsey', 'Freund', 'Savannah', 'Clark', 'Bradley', 'Monsell', 'Daisha', 'Schmidt', 'Airabella', 'Koontz', 'Hailey', 'Malle', 'Devon', 'Miranda', 'Danielle', 'Nguyen', 'Mateo', 'Cisneros', 'William', 'Pablo', 'Jason', 'Hundsdorfer', 'Antonio', 'Desai', 'Rachel', 'Bakeman', 'Mamdooh', 'el-Moustafa',  'Aaron', 'Knott', 'Jessica', 'Greenberg', 'Lexi', 'Hatton', 'Jesse', 'Hodapp', 'Andrew', 'Brunelli', 'Makenzie', 'Swann', 'Carlos', 'Anaya','Beatty', 'Melissa', 'Bickel', 'Rachel', 'Boh', 'Anna', 'Yoshimura', 'Joseph', 'Hazelton', 'Tiffany', 'Nguyen', 'Ryan', 'Tyler', 'Max', 'Flores',  'Terri', 'Mergelman', 'Abigail', 'Orgeron', 'Jessica', 'Huynh', 'Kyle', 'Blanscet', 'Ronald', 'Toth', 'Branden', 'Cantrell', 'Loughran', 'Michael', 'Melendrez', 'Katie', 'Abercrombie', 'Justin', 'Krause', 'Jennifer', 'Hauge', 'Tiffanie', 'Her', 'Dyllan', 'Paige', 'Cole', 'Hathcoat','Inhulsen', 'Tessa', 'Rawanduzy', 'Vanessa', 'Gonzalez'],
    #        "hr":[ 'Lindsey', 'Carter', 'Duncan', 'Kruse', 'Callahan', 'Foster', 'Jamie', 'Ortiz', 'Ryan', 'Barrett', 'Samuel', 'Palmer', 'Riley', 'Mcloughlin', 'Aimee', 'Apelyan', 'Maryah', 'Falloon', 'Lucille', 'Mitchell', 'Christian', 'Zambrano', 'Munoz', 'Bryce', 'Vaillancourt', 'Brandilyn', 'Collins', 'Konner', 'Gearhart', 'Andrew', 'Houghton', 'Marisa', 'Ramey', 'Magdalynne', 'Noah', 'Megan', 'Salamena', 'Meghan', 'Arnold', 'James', 'Rice', 'Wesley', 'Nunn', 'Gareth', 'Newkirk', 'Austin', 'Harline', 'Courtney', 'Martinez', 'Alexandra', 'Graham', 'Alexander', 'Swearingen', 'Brandy', 'Waldner', 'Coleman', 'Keelen', 'Casey', 'Buhr', 'Shauna', 'Sneed', 'Caitlin', 'Dean', 'Andrew', 'Kirin', 'Nadia', 'Minks', 'Ivy', 'Lucero', 'Kevin', 'Curry', 'Charles', 'Cramer', 'Emily', 'Warner', 'Mckenzie', 'Haycock', 'Faviola', 'Soto', 'Stephen', 'Wharton', 'Alexandria', 'Fortner', 'Savannah', 'Kivett', 'Tanner', 'Jones', 'Luisa', 'Bautista', 'Juhaina', 'al-Bilal', 'Siena', 'Ingram', 'Alondra', 'Gardea', 'Corral', 'Vincent', 'Webster', 'Abdul', 'Felipe', 'Martinez', 'Acosta', 'Emma', 'Casias', 'Adolf', 'Malik', 'Christian', 'Chow', 'Asad', 'el-Yacoub', 'Holly', 'Marshall',  'Veronica', 'Tounzen', 'Haley', 'Ingrim', 'Hyrup', 'Kayla', 'Sandefur', 'Rylee', 'Onstott', 'Kelli', 'Bartolome', 'Thomas', 'Chanlynn', 'Hannah', 'Ratterman', 'Alexandria', 'Winter', 'Ryan', 'Russell', 'Logan', 'Nighswonger', 'Zaghlool', 'al-Pasha', 'Madeline', 'Kremke','Jesse', 'Carballo', 'Robert', 'Podolski', 'Viridiana', 'Ballesteros', 'Michael', 'Griffin', 'Chad', 'Klemp', 'Weldon', 'Hightower', 'Daniel', 'Pierce', 'Austin', 'Haas', 'Madison', 'Fithian', 'Zachary'],
    #        "db1":[ 'Lindsey', 'Carter', 'Duncan', 'Kruse', 'Callahan', 'Foster', 'Jamie', 'Ortiz', 'Ryan', 'Barrett', 'Samuel', 'Palmer', 'Riley', 'Mcloughlin', 'Aimee', 'Apelyan', 'Maryah', 'Falloon', 'Lucille', 'Mitchell', 'Christian', 'Zambrano', 'Munoz', 'Bryce', 'Vaillancourt', 'Brandilyn', 'Collins', 'Konner', 'Gearhart', 'Andrew', 'Houghton', 'Marisa', 'Ramey', 'Magdalynne', 'Noah', 'Megan', 'Salamena', 'Meghan', 'Arnold', 'James', 'Rice', 'Wesley', 'Nunn', 'Gareth', 'Newkirk', 'Austin', 'Harline', 'Courtney', 'Martinez', 'Alexandra', 'Graham', 'Alexander', 'Swearingen', 'Brandy', 'Waldner', 'Coleman', 'Keelen', 'Casey', 'Buhr', 'Shauna', 'Sneed', 'Caitlin', 'Dean', 'Andrew', 'Kirin', 'Nadia', 'Minks', 'Ivy', 'Lucero', 'Kevin', 'Curry', 'Charles', 'Cramer', 'Emily', 'Warner', 'Mckenzie', 'Haycock', 'Faviola', 'Soto', 'Stephen', 'Wharton', 'Alexandria', 'Fortner', 'Savannah', 'Kivett', 'Tanner', 'Jones', 'Luisa', 'Bautista', 'Juhaina', 'al-Bilal', 'Siena', 'Ingram', 'Alondra', 'Gardea', 'Corral', 'Vincent', 'Webster', 'Abdul', 'Felipe', 'Martinez', 'Acosta', 'Emma', 'Casias', 'Adolf', 'Malik', 'Christian', 'Chow', 'Asad', 'el-Yacoub', 'Holly', 'Marshall',  'Veronica', 'Tounzen', 'Haley', 'Ingrim', 'Hyrup', 'Kayla', 'Sandefur', 'Rylee', 'Onstott', 'Kelli', 'Bartolome', 'Thomas', 'Chanlynn', 'Hannah', 'Ratterman', 'Alexandria', 'Winter', 'Ryan', 'Russell', 'Logan', 'Nighswonger', 'Zaghlool', 'al-Pasha', 'Madeline', 'Kremke','Jesse', 'Carballo', 'Robert', 'Podolski', 'Viridiana', 'Ballesteros', 'Michael', 'Griffin', 'Chad', 'Klemp', 'Weldon', 'Hightower', 'Daniel', 'Pierce', 'Austin', 'Haas', 'Madison', 'Fithian', 'Zachary'],
    #        "pl2":[ 'Lindsey', 'Carter', 'Duncan', 'Kruse', 'Callahan', 'Foster', 'Jamie', 'Ortiz', 'Ryan', 'Barrett', 'Samuel', 'Palmer', 'Riley', 'Mcloughlin', 'Aimee', 'Apelyan', 'Maryah', 'Falloon', 'Lucille', 'Mitchell', 'Christian', 'Zambrano', 'Munoz', 'Bryce', 'Vaillancourt', 'Brandilyn', 'Collins', 'Konner', 'Gearhart', 'Andrew', 'Houghton', 'Marisa', 'Ramey', 'Magdalynne', 'Noah', 'Megan', 'Salamena', 'Meghan', 'Arnold', 'James', 'Rice', 'Wesley', 'Nunn', 'Gareth', 'Newkirk', 'Austin', 'Harline', 'Courtney', 'Martinez', 'Alexandra', 'Graham', 'Alexander', 'Swearingen', 'Brandy', 'Waldner', 'Coleman', 'Keelen', 'Casey', 'Buhr', 'Shauna', 'Sneed', 'Caitlin', 'Dean', 'Andrew', 'Kirin', 'Nadia', 'Minks', 'Ivy', 'Lucero', 'Kevin', 'Curry', 'Charles', 'Cramer', 'Emily', 'Warner', 'Mckenzie', 'Haycock', 'Faviola', 'Soto', 'Stephen', 'Wharton', 'Alexandria', 'Fortner', 'Savannah', 'Kivett', 'Tanner', 'Jones', 'Luisa', 'Bautista', 'Juhaina', 'al-Bilal', 'Siena', 'Ingram', 'Alondra', 'Gardea', 'Corral', 'Vincent', 'Webster', 'Abdul', 'Felipe', 'Martinez', 'Acosta', 'Emma', 'Casias', 'Adolf', 'Malik', 'Christian', 'Chow', 'Asad', 'el-Yacoub', 'Holly', 'Marshall',  'Veronica', 'Tounzen', 'Haley', 'Ingrim', 'Hyrup', 'Kayla', 'Sandefur', 'Rylee', 'Onstott', 'Kelli', 'Bartolome', 'Thomas', 'Chanlynn', 'Hannah', 'Ratterman', 'Alexandria', 'Winter', 'Ryan', 'Russell', 'Logan', 'Nighswonger', 'Zaghlool', 'al-Pasha', 'Madeline', 'Kremke','Jesse', 'Carballo', 'Robert', 'Podolski', 'Viridiana', 'Ballesteros', 'Michael', 'Griffin', 'Chad', 'Klemp', 'Weldon', 'Hightower', 'Daniel', 'Pierce', 'Austin', 'Haas', 'Madison', 'Fithian', 'Zachary']}

    list_2016 = [20160001, 20160002, 20160003, 20160004, 20160005, 20160006, 20160007, 20160008, 20160009, 20160010,
                 20160011, 20160012, 20160013, 20160014, 20160015, 20160016, 20160017, 20160018, 20160019, 20160020,
                 20160021, 20160022, 20160023, 20160024, 20160025, 20160026, 20160027, 20160028, 20160029, 20160030,
                 20160031, 20160032, 20160033, 20160034, 20160035, 20160036, 20160037, 20160038, 20160039, 20160040,
                 20160041, 20160042, 20160043, 20160044, 20160045, 20160046, 20160047, 20160048, 20160049, 20160050,
                 20160051, 20160052, 20160053, 20160054, 20160055, 20160056, 20160057, 20160058, 20160059, 20160060,
                 20160061, 20160062, 20160063, 20160064, 20160065, 20160066, 20160067, 20160068, 20160069, 20160070,
                 20160071, 20160072, 20160073, 20160074, 20160075, 20160076, 20160077, 20160078, 20160079, 20160080,
                 20160081, 20160082, 20160083, 20160084, 20160085, 20160086, 20160087, 20160088, 20160089, 20160090,
                 20160091, 20160092, 20160093, 20160094, 20160095, 20160096, 20160097, 20160098, 20160099, 20160100,
                 20160101, 20160102, 20160103, 20160104, 20160105, 20160106, 20160107, 20160108, 20160109, 20160110,
                 20160111, 20160112, 20160113, 20160114, 20160115, 20160116, 20160117, 20160118, 20160119, 20160120,
                 20160121, 20160122, 20160123, 20160124, 20160125, 20160126, 20160127, 20160128, 20160129, 20160130,
                 20160131, 20160132, 20160133, 20160134, 20160135, 20160136, 20160137, 20160138, 20160139, 20160140,
                 20160141, 20160142, 20160143, 20160144, 20160145, 20160146, 20160147, 20160148, 20160149, 20160150,
                 20160151, 20160152, 20160153, 20160154, 20160155, 20160156, 20160157, 20160158, 20160159, 20160160,
                 20160161, 20160162, 20160163, 20160164, 20160165, 20160166, 20160167, 20160168, 20160169, 20160170,
                 20160171, 20160172, 20160173, 20160174, 20160175, 20160176, 20160177, 20160178, 20160179, 20160180,
                 20160181, 20160182, 20160183, 20160184, 20160185, 20160186, 20160187, 20160188, 20160189, 20160190,
                 20160191, 20160192, 20160193, 20160194, 20160195, 20160196, 20160197, 20160198, 20160199, 20160200,
                 20160201, 20160202, 20160203, 20160204, 20160205, 20160206, 20160207, 20160208, 20160209, 20160210,
                 20160211, 20160212, 20160213, 20160214, 20160215, 20160216, 20160217, 20160218, 20160219, 20160220,
                 20160221, 20160222, 20160223, 20160224, 20160225, 20160226, 20160227, 20160228, 20160229, 20160230,
                 20160231, 20160232, 20160233, 20160234, 20160235, 160236, 20160237, 20160238, 20160239, 20160240,
                 20160241, 20160242, 20160243, 20160244, 20160245, 20160246, 20160247, 20160248, 20160249, 20160250,
                 20160251, 20160252, 20160253, 20160254, 20160255, 20160256, 20160257, 20160258, 20160259, 20160260,
                 20160261, 20160262, 20160263, 20160264, 20160265, 20160266, 20160267, 20160268, 20160269, 20160270,
                 20160271, 20160272, 20160273, 20160274, 20160275, 20160276, 20160277, 20160278, 20160279, 20160280,
                 20160281, 20160282, 20160283, 20160284, 20160285, 20160286, 20160287, 20160288, 20160289, 20160290,
                 20160291, 20160292, 20160293, 20160294, 20160295, 20160296, 20160297, 20160298]
    list_2017 = [20170001, 20170002, 20170003, 20170004, 20170005, 20170006, 20170007, 20170008, 20170009, 20170010,
                 20170011, 20170012, 20170013, 20170014, 20170015, 20170016, 20170017, 20170018, 20170019, 20170020,
                 20170021, 20170022, 20170023, 20170024, 20170025, 20170026, 20170027, 20170028, 20170029, 20170030,
                 20170031, 20170032, 20170033, 20170034, 20170035, 20170036, 20170037, 20170038, 20170039, 20170040,
                 20170041, 20170042, 20170043, 20170044, 20170045, 20170046, 20170047, 20170048, 20170049, 20170050,
                 20170051, 20170052, 20170053, 20170054, 20170055, 20170056, 20170057, 20170058, 20170059, 20170060,
                 20170061, 20170062, 20170063, 20170064, 20170065, 20170066, 20170067, 20170068, 20170069, 20170070,
                 20170071, 20170072, 20170073, 20170074, 20170075, 20170076, 20170077, 20170078, 20170079, 20170080,
                 20170081, 20170082, 20170083, 20170084, 20170085, 20170086, 20170087, 20170088, 20170089, 20170090,
                 20170091, 20170092, 20170093, 20170094, 20170095, 20170096, 20170097, 20170098, 20170099, 20170100,
                 20170101, 20170102, 20170103, 20170104, 20170105, 20170106, 20170107, 20170108, 20170109, 20170110,
                 20170111, 20170112, 20170113, 20170114, 20170115, 20170116, 20170117, 20170118, 20170119, 20170120,
                 20170121, 20170122, 20170123, 20170124, 20170125, 20170126, 20170127, 20170128, 20170129, 20170130,
                 20170131, 20170132, 20170133, 20170134, 20170135, 20170136, 20170137, 20170138, 20170139, 20170140,
                 20170141, 20170142, 20170143, 20170144, 20170145, 20170146, 20170147, 20170148, 20170149, 20170150,
                 20170151, 20170152, 20170153, 20170154, 20170155, 20170156, 20170157, 20170158, 20170159, 20170160,
                 20170161, 20170162, 20170163, 20170164, 20170165, 20170166, 20170167, 20170168, 20170169, 20170170,
                 20170171, 20170172, 20170173, 20170174, 20170175, 20170176, 20170177, 20170178, 20170179, 20170180,
                 20170181, 20170182, 20170183, 20170184, 20170185, 20170186, 20170187, 20170188, 20170189, 20170190,
                 20170191, 20170192, 20170193, 20170194, 20170195, 20170196, 20170197, 20170198, 20170199, 20170200,
                 20170201, 20170202, 20170203, 20170204, 20170205, 20170206, 20170207, 20170208, 20170209, 20170210,
                 20170211, 20170212, 20170213, 20170214, 20170215, 20170216, 20170217, 20170218, 20170219, 20170220,
                 20170221, 20170222, 20170223, 20170224, 20170225, 20170226, 20170227, 20170228, 20170229, 20170230,
                 20170231, 20170232, 20170233, 20170234, 20170235, 160236, 20170237, 20170238, 20170239, 20170240,
                 20170241, 20170242, 20170243, 20170244, 20170245, 20170246, 20170247, 20170248, 20170249, 20170250,
                 20170251, 20170252, 20170253, 20170254, 20170255, 20170256, 20170257, 20170258, 20170259, 20170260,
                 20170261, 20170262, 20170263, 20170264, 20170265, 20170266, 20170267, 20170268, 20170269, 20170270,
                 20170271, 20170272, 20170273, 20170274, 20170275, 20170276, 20170277, 20170278, 20170279, 20170280,
                 20170281, 20170282, 20170283, 20170284, 20170285, 20170286, 20170287, 20170288, 20170289, 20170290,
                 20170291, 20170292, 20170293, 20170294, 20170295, 20170296, 20170297, 20170298]
    list_2018 = [20180001, 20180002, 20180003, 20180004, 20180005, 20180006, 20180007, 20180008, 20180009, 20180010,
                 20180011, 20180012, 20180013, 20180014, 20180015, 20180016, 20180017, 20180018, 20180019, 20180020,
                 20180021, 20180022, 20180023, 20180024, 20180025, 20180026, 20180027, 20180028, 20180029, 20180030,
                 20180031, 20180032, 20180033, 20180034, 20180035, 20180036, 20180037, 20180038, 20180039, 20180040,
                 20180041, 20180042, 20180043, 20180044, 20180045, 20180046, 20180047, 20180048, 20180049, 20180050,
                 20180051, 20180052, 20180053, 20180054, 20180055, 20180056, 20180057, 20180058, 20180059, 20180060,
                 20180061, 20180062, 20180063, 20180064, 20180065, 20180066, 20180067, 20180068, 20180069, 20180070,
                 20180071, 20180072, 20180073, 20180074, 20180075, 20180076, 20180077, 20180078, 20180079, 20180080,
                 20180081, 20180082, 20180083, 20180084, 20180085, 20180086, 20180087, 20180088, 20180089, 20180090,
                 20180091, 20180092, 20180093, 20180094, 20180095, 20180096, 20180097, 20180098, 20180099, 20180100,
                 20180101, 20180102, 20180103, 20180104, 20180105, 20180106, 20180107, 20180108, 20180109, 20180110,
                 20180111, 20180112, 20180113, 20180114, 20180115, 20180116, 20180117, 20180118, 20180119, 20180120,
                 20180121, 20180122, 20180123, 20180124, 20180125, 20180126, 20180127, 20180128, 20180129, 20180130,
                 20180131, 20180132, 20180133, 20180134, 20180135, 20180136, 20180137, 20180138, 20180139, 20180140,
                 20180141, 20180142, 20180143, 20180144, 20180145, 20180146, 20180147, 20180148, 20180149, 20180150,
                 20180151, 20180152, 20180153, 20180154, 20180155, 20180156, 20180157, 20180158, 20180159, 20180160,
                 20180161, 20180162, 20180163, 20180164, 20180165, 20180166, 20180167, 20180168, 20180169, 20180170,
                 20180171, 20180172, 20180173, 20180174, 20180175, 20180176, 20180177, 20180178, 20180179, 20180180,
                 20180181, 20180182, 20180183, 20180184, 20180185, 20180186, 20180187, 20180188, 20180189, 20180190,
                 20180191, 20180192, 20180193, 20180194, 20180195, 20180196, 20180197, 20180198, 20180199, 20180200,
                 20180201, 20180202, 20180203, 20180204, 20180205, 20180206, 20180207, 20180208, 20180209, 20180210,
                 20180211, 20180212, 20180213, 20180214, 20180215, 20180216, 20180217, 20180218, 20180219, 20180220,
                 20180221, 20180222, 20180223, 20180224, 20180225, 20180226, 20180227, 20180228, 20180229, 20180230,
                 20180231, 20180232, 20180233, 20180234, 20180235, 160236, 20180237, 20180238, 20180239, 20180240,
                 20180241, 20180242, 20180243, 20180244, 20180245, 20180246, 20180247, 20180248, 20180249, 20180250,
                 20180251, 20180252, 20180253, 20180254, 20180255, 20180256, 20180257, 20180258, 20180259, 20180260,
                 20180261, 20180262, 20180263, 20180264, 20180265, 20180266, 20180267, 20180268, 20180269, 20180270,
                 20180271, 20180272, 20180273, 20180274, 20180275, 20180276, 20180277, 20180278, 20180279, 20180280,
                 20180281, 20180282, 20180283, 20180284, 20180285, 20180286, 20180287, 20180288, 20180289, 20180290,
                 20180291, 20180292, 20180293, 20180294, 20180295, 20180296, 20180297, 20180298]
    list_2019 = [20190001, 20190002, 20190003, 20190004, 20190005, 20190006, 20190007, 20190008, 20190009, 20190010,
                 20190011, 20190012, 20190013, 20190014, 20190015, 20190016, 20190017, 20190018, 20190019, 20190020,
                 20190021, 20190022, 20190023, 20190024, 20190025, 20190026, 20190027, 20190028, 20190029, 20190030,
                 20190031, 20190032, 20190033, 20190034, 20190035, 20190036, 20190037, 20190038, 20190039, 20190040,
                 20190041, 20190042, 20190043, 20190044, 20190045, 20190046, 20190047, 20190048, 20190049, 20190050,
                 20190051, 20190052, 20190053, 20190054, 20190055, 20190056, 20190057, 20190058, 20190059, 20190060,
                 20190061, 20190062, 20190063, 20190064, 20190065, 20190066, 20190067, 20190068, 20190069, 20190070,
                 20190071, 20190072, 20190073, 20190074, 20190075, 20190076, 20190077, 20190078, 20190079, 20190080,
                 20190081, 20190082, 20190083, 20190084, 20190085, 20190086, 20190087, 20190088, 20190089, 20190090,
                 20190091, 20190092, 20190093, 20190094, 20190095, 20190096, 20190097, 20190098, 20190099, 20190100,
                 20190101, 20190102, 20190103, 20190104, 20190105, 20190106, 20190107, 20190108, 20190109, 20190110,
                 20190111, 20190112, 20190113, 20190114, 20190115, 20190116, 20190117, 20190118, 20190119, 20190120,
                 20190121, 20190122, 20190123, 20190124, 20190125, 20190126, 20190127, 20190128, 20190129, 20190130,
                 20190131, 20190132, 20190133, 20190134, 20190135, 20190136, 20190137, 20190138, 20190139, 20190140,
                 20190141, 20190142, 20190143, 20190144, 20190145, 20190146, 20190147, 20190148, 20190149, 20190150,
                 20190151, 20190152, 20190153, 20190154, 20190155, 20190156, 20190157, 20190158, 20190159, 20190160,
                 20190161, 20190162, 20190163, 20190164, 20190165, 20190166, 20190167, 20190168, 20190169, 20190170,
                 20190171, 20190172, 20190173, 20190174, 20190175, 20190176, 20190177, 20190178, 20190179, 20190180,
                 20190181, 20190182, 20190183, 20190184, 20190185, 20190186, 20190187, 20190188, 20190189, 20190190,
                 20190191, 20190192, 20190193, 20190194, 20190195, 20190196, 20190197, 20190198, 20190199, 20190200,
                 20190201, 20190202, 20190203, 20190204, 20190205, 20190206, 20190207, 20190208, 20190209, 20190210,
                 20190211, 20190212, 20190213, 20190214, 20190215, 20190216, 20190217, 20190218, 20190219, 20190220,
                 20190221, 20190222, 20190223, 20190224, 20190225, 20190226, 20190227, 20190228, 20190229, 20190230,
                 20190231, 20190232, 20190233, 20190234, 20190235, 160236, 20190237, 20190238, 20190239, 20190240,
                 20190241, 20190242, 20190243, 20190244, 20190245, 20190246, 20190247, 20190248, 20190249, 20190250,
                 20190251, 20190252, 20190253, 20190254, 20190255, 20190256, 20190257, 20190258, 20190259, 20190260,
                 20190261, 20190262, 20190263, 20190264, 20190265, 20190266, 20190267, 20190268, 20190269, 20190270,
                 20190271, 20190272, 20190273, 20190274, 20190275, 20190276, 20190277, 20190278, 20190279, 20190280,
                 20190281, 20190282, 20190283, 20190284, 20190285, 20190286, 20190287, 20190288, 20190289, 20190290,
                 20190291, 20190292, 20190293, 20190294, 20190295, 20190296, 20190297, 20190298]

    cat = {
        "mm": list_2019,
        "ds": list_2016,
        "ai": list_2016,
        "co": list_2016,
        "os2": list_2016,
        "concepts": list_2016,
        "ethics": list_2016,
        "db2": list_2016,
        "ir": list_2017,
        "logic": list_2017,
        "or": list_2017,
        "pat": list_2017,
        "cs": list_2017,
        "is": list_2017,
        "math1": list_2017,
        "eng1": list_2018,
        "phy": list_2018,
        "elec": list_2018,
        "econ": list_2018,
        "it": list_2018,
        "math2": list_2018,
        "stat": list_2018,
        "eng2": list_2019,
        "pl": list_2019,
        "algo": list_2019,
        "hr": list_2019,
        "db1": list_2019,
        "pl2": list_2019}

    def __init__(self):
        self._rooms = []
        self._TimeAvilable = []
        self._instructors = []
        self._students = []
        # self._studentcategory = {}

        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.Time_Avilable)):
            self._TimeAvilable.append(TimeAvilable(self.Time_Avilable[i][0], self.Time_Avilable[i][1], self.Time_Avilable[i][2] ,self.Time_Avilable[i][3]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        # for i in range(0, len(self.STUDENT)):
        #     self._students.append(Student(self.STUDENT[i][0], self.STUDENT[i][1], self.STUDENT[i][2]))
        # if self.STUDENT[i][2] in self._studentcategory:
        #     stu = self._studentcategory[self.STUDENT[i][2]]
        #     self._studentcategory[self.STUDENT[i][2]] = stu + self.STUDENT[i][1]
        # else:
        #     self._studentcategory[self.STUDENT[i][2]] =  self.STUDENT[i][1]
        course1 = Courses("C1", "mm", [self._instructors[0], self._instructors[1]], self.cat["mm"],
                          len(self.cat["mm"]))  # (code, name, instructors,students, maxNumbOfStudents)
        course2 = Courses("C2", "pl", [self._instructors[0], self._instructors[1], self._instructors[2]],
                          self.cat["pl"], len(self.cat["pl"]))
        course3 = Courses("C3", "ir", [self._instructors[0], self._instructors[1]], self.cat["ir"], len(self.cat["ir"]))
        course4 = Courses("C4", "or", [self._instructors[2], self._instructors[3]], self.cat["or"], len(self.cat["or"]))
        course5 = Courses("C5", "ds", [self._instructors[3]], self.cat["ds"], len(self.cat["ds"]))
        course6 = Courses("C6", "logic", [self._instructors[0], self._instructors[2]], self.cat["logic"],
                          len(self.cat["logic"]))
        course7 = Courses("C7", "pat", [self._instructors[1], self._instructors[3]], self.cat["pat"],
                          len(self.cat["pat"]))
        course8 = Courses("C8", "cs", [self._instructors[2], self._instructors[3]], self.cat["cs"], len(self.cat["cs"]))
        course9 = Courses("C9", "is", [self._instructors[1], self._instructors[3]], self.cat["is"], len(self.cat["is"]))
        course10 = Courses("C10", "math1", [self._instructors[1], self._instructors[3]], self.cat["math1"],
                           len(self.cat["math1"]))
        course11 = Courses("C11", "eng1", [self._instructors[2], self._instructors[3]], self.cat["eng1"],
                           len(self.cat["eng1"]))
        course12 = Courses("C12", "elec", [self._instructors[0], self._instructors[1], self._instructors[2]],
                           self.cat["elec"], len(self.cat["elec"]))
        course13 = Courses("C13", "phy", [self._instructors[1], self._instructors[3]], self.cat["phy"],
                           len(self.cat["phy"]))
        course14 = Courses("C14", "econ", [self._instructors[2], self._instructors[3]], self.cat["econ"],
                           len(self.cat["econ"]))
        course15 = Courses("C15", "it", [self._instructors[0], self._instructors[1], self._instructors[2]],
                           self.cat["it"], len(self.cat["it"]))
        course16 = Courses("C16", "math2", [self._instructors[1], self._instructors[3]], self.cat["math2"],
                           len(self.cat["math2"]))
        course17 = Courses("C17", "algo", [self._instructors[3]], self.cat["algo"], len(self.cat["algo"]))
        course18 = Courses("C18", "stat", [self._instructors[2], self._instructors[3]], self.cat["stat"],
                           len(self.cat["stat"]))
        course19 = Courses("C19", "eng2", [self._instructors[1], self._instructors[3]], self.cat["eng2"],
                           len(self.cat["eng2"]))
        course20 = Courses("C20", "db1", [self._instructors[2], self._instructors[3]], self.cat["db1"],
                           len(self.cat["db1"]))
        course21 = Courses("C21", "hr", [self._instructors[2], self._instructors[3]], self.cat["hr"],
                           len(self.cat["hr"]))
        course22 = Courses("C22", "pl2", [self._instructors[0], self._instructors[1], self._instructors[2]],
                           self.cat["pl2"], len(self.cat["pl2"]))
        course23 = Courses("C23", "ai", [self._instructors[2], self._instructors[3]], self.cat["ai"],
                           len(self.cat["ai"]))
        course24 = Courses("C24", "co", [self._instructors[2], self._instructors[3]], self.cat["co"],
                           len(self.cat["co"]))
        course25 = Courses("C25", "os2", [self._instructors[0], self._instructors[3]], self.cat["os2"],
                           len(self.cat["os2"]))
        course26 = Courses("C26", "concepts", [self._instructors[2], self._instructors[0]], self.cat["concepts"],
                           len(self.cat["concepts"]))
        course27 = Courses("C27", "ethics", [self._instructors[0], self._instructors[1]], self.cat["ethics"],
                           len(self.cat["ethics"]))
        course28 = Courses("C28", "db2", [self._instructors[0], self._instructors[2]], self.cat["db2"],
                           len(self.cat["db2"]))

        self._courses = [course1, course2, course3, course4, course5, course6, course7, course8, course9, course10,
                         course11, course12, course13, course14, course15, course16, course17, course18, course19,
                         course20, course21, course22, course23, course24, course25, course26, course27, course28]
        dept1 = Department("Cs", [course1, course3, course8, course9, course16, course17, course22, course23, course24,
                                  course25, course26])
        dept2 = Department("Is",
                           [course2, course4, course10, course14, course15, course18, course19, course27, course28,
                            course5])
        dept3 = Department("It", [course6, course7, course11, course12, course13, course20, course21])
        self.depts = [dept1, dept2, dept3]
        self.numberOfClasses = 0
        for i in range(0, len(self.depts)):
            self.numberOfClasses += len(self.depts[i].get_Courses())
        # self.numberOfClasses = len(self._courses)

    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors

    def get_students(self):
        return self._students

    def get_courses(self):
        return self._courses

    def get_depts(self):
        return self.depts

    def get_TimeAvilable(self):
        return self._TimeAvilable

    def get_numberOfClasses(self):
        return self.numberOfClasses


###################################################
class Exam:
    def __init__(self, id, dept, course, students):
        self._id = id
        self._dept = dept
        self._course = course
        self._students = students
        # the rest will be assigned random
        self._instructor = None
        self._TimeAvilable = None
        self._room = None

    def get_id(self): return self._id

    def get_dept(self): return self._dept

    def get_course(self): return self._course

    def get_students(self): return self._students

    def get_instructor(self): return self._instructor

    def get_TimeAvilable(self): return self._TimeAvilable

    def get_room(self): return self._room

    # to be set random
    def set_instructor(self, instructor): self._instructor = instructor

    def set_TimeAvilable(self, TimeAvilable): self._TimeAvilable = TimeAvilable

    def set_room(self, room): self._room = room

    def __str__(self):  # used in display class
        return "{" + str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(
            self._TimeAvilable.get_id()) + "," + str(len(self._students)) + "}"


class schedule:
    def __init__(self):
        self.data = data
        self.exams = []  # of the schedule instances
        self.num_of_conflict = 0
        self.fitness = -1
        self.examcounter = 0  # counter to use in the initialization func
        self.isFitnesschanged = True

    def initialize(self):
        depts = self.data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_Courses()
            for j in range(0, len(courses)):
                new_exam = Exam(self.examcounter, depts[i], courses[j], courses[j].get_students())
                self.examcounter += 1
                new_exam.set_TimeAvilable(data.get_TimeAvilable()[randint(0, len(data.get_TimeAvilable()) - 1)])
                new_exam.set_room(data.get_rooms()[randint(0, len(data.get_rooms()) - 1)])
                new_exam.set_instructor(courses[j].get_instructors()[randint(0, len(courses[j].get_instructors()) - 1)])
                self.exams.append(new_exam)
        return self

    def get_exams(self):  # mohema fe class GA
        return self.exams

    def get_number_Of_conflict(self):
        return self.num_of_conflict

    def calculate_fit(self):
        self.num_of_conflict = 0
        self.isFitnesschanged = True
        exams = self.get_exams()
        for i in range(0, len(exams)):

            if (exams[i].get_room().get_seatingCapacity() < exams[i].get_course().get_maxNumbOfStudents()):
                self.num_of_conflict += 1
            for j in range(0, len(exams)):
                if (j >= i):
                    if (exams[i].get_TimeAvilable() == exams[j].get_TimeAvilable() and exams[i].get_id() != exams[
                        j].get_id()):
                        if (exams[i].get_room() == exams[j].get_room()): self.num_of_conflict += 1
                        # if (exams[i].get_instructor() == exams[j].get_instructor()): self.num_of_conflict += 1
                        # lists of students need to be alphabetically ordered
                        if (
                        not set(exams[i].get_students()).isdisjoint(exams[j].get_students())): self.num_of_conflict += 1
                        # if (classes[i].get_students() == classes[j].get_students()): self.num_of_conflict += 1
        return 1 / ((1.0 * self.num_of_conflict) + 1)  # *1.0 to convert int to float

    def get_fitness(self):
        if (self.isFitnesschanged == True):
            self.fitness = self.calculate_fit()
            self.isFitnesschanged = False
        return self.fitness

    def __str__(self):
        pharse = ""
        for i in range(0, len(self.exams)):
            pharse += str(self.exams[i]) + ","

        return pharse


class Population:
    def __init__(self, size):
        self.size = size
        self.data = data  # mlhaaa4 lazma t2rebn
        self.schedules = []
        for i in range(0, size):
            self.schedules.append(schedule().initialize())

    def get_schedules(self):
        return self.schedules


############################## L7d hena done ^_^
class genatic_algorithm:

    def evolve(self, popu):  # de bs elly bst5dmha direct fe el main w hia btst5dm elly t7tha
        return self.mutation(self.crossover(popu))

    def crossover(self, popu):
        crossover_pop = Population(0)
        for i in range(NUMB_OFELITE_SCHEDULES):
            crossover_pop.get_schedules().append(
                popu.get_schedules()[i])  # take a copy of population list not reference(only the last 9)
        # i = NUMB_OFELITE_SCHEDULES
        i = 0
        while i < POPULATION_SIZE:
            schedule1 = self.select_tournament_population(popu).get_schedules()[0]
            schedule2 = self.select_tournament_population(popu).get_schedules()[1]
            crossover_pop.get_schedules().append(self.crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def mutation(self, popu):  # mutate every schedule in population
        for i in range(0, POPULATION_SIZE):  # NUMB_OFELITE_SCHEDULES
            self.mutate_schedule(popu.get_schedules()[i])
        return popu

    def crossover_schedule(self, schedule1, schedule2):  # get new childe from restored  2 schduler parent
        crossoverSchedule = schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_exams())):
            if (random() > 0.5):
                crossoverSchedule.get_exams()[i] = schedule1.get_exams()[i]
            else:
                crossoverSchedule.get_exams()[i] = schedule2.get_exams()[i]
        return crossoverSchedule

    def mutate_schedule(self, mutate):  # mutate 1 schedule
        scheduler = schedule().initialize()
        for i in range(0, len(mutate.get_exams())):
            if (MUTATION_RATE > random()):
                mutate.get_exams()[i] = scheduler.get_exams()[i]
        return mutate

    def select_tournament_population(self, popu):  # to select parents
        tournament_pop = Population(0)
        i = 0
        while i < TORNAMENT_SELECTON_SIZE:
            tournament_pop.get_schedules().append(popu.get_schedules()[randint(0, POPULATION_SIZE - 1)])
            i += 1
        tournament_pop.get_schedules().sort(key=get_sort_key, reverse=True)
        return tournament_pop


class Display:
    def print_available_data(self):
        print("> ALL Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_Time_Avilable()

    def print_dept(self):
        depts = data.get_depts()
        print(len(depts))
        availableDeptsTable = prettytable.PrettyTable(['dept', 'course'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_Courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])

        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(['id', 'course #', 'max # of students', 'instructors'])
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ","
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr])
        print(availableCoursesTable)

    def print_instructor(self):
        data = Data()
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructors'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])

        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)

    def print_Time_Avilable(self):
        availableTimeAvilableTable = prettytable.PrettyTable(['id', 'Time', 'day', 'date'])
        timeAvilable = data.get_TimeAvilable()
        for i in range(0, len(timeAvilable)):
            availableTimeAvilableTable.add_row([timeAvilable[i].get_id(), timeAvilable[i].get_time(), timeAvilable[i].get_day() , timeAvilable[i].get_date()])
        print(availableTimeAvilableTable)

    def get_Time_slots(self):
        timeslots = []
        timeAvilable = data.get_TimeAvilable()
        for i in range(0, len(timeAvilable)):
            if timeAvilable[i].get_time() not in timeslots:
                timeslots.append(timeAvilable[i].get_time())
        return timeslots

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            ['schedule #', 'fitness', '# of conflicts', 'classes[dept,course,room,instructor,no of students]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_number_Of_conflict(), schedules[i]])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_exams()
        table = prettytable.PrettyTable(
            ['Exam #', 'Dept', 'Course(number , max # of students)', 'Room (Capacity)', 'Instructor', 'TimeAvilable'])
        for i in range(0, len(classes)):
            table.add_row([
                str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " + str(
                classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           classes[i].get_room().get_number() + " (" + str(
                               classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name() + " (" + str(
                               classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_TimeAvilable().get_time() + " (" + str(
                               classes[i].get_TimeAvilable().get_id()) + ")" + " " +
                           classes[i].get_TimeAvilable().get_day() + " " +
                           classes[i].get_TimeAvilable().get_date()
                          ])
        print(table)

    def save_schedule_as_model(self, schedule):
        exams = []
        classes = schedule.get_exams()
        for i in range(0, len(classes)):
            exams.append([classes[i].get_course().get_name(), classes[i].get_room().get_number(),  classes[i].get_TimeAvilable().get_day() ,  classes[i].get_TimeAvilable().get_date(),  classes[i].get_TimeAvilable().get_time()])
        # exams.sort(key=sort_by_id)
        exams.sort(key=sort_by_id)
        return exams

data = Data()  # used in schedule class
POPULATION_SIZE = 10
NUMB_OFELITE_SCHEDULES = 1  ####
TORNAMENT_SELECTON_SIZE = 2  ####  no of parents
MUTATION_RATE = 0.1  ####

def get_sort_key(list):
    return list.get_fitness()  # de func mwgoda fe class schedule

def sort_by_id(exams):
    return datetime.strptime(exams[3],"%d/%m")


def generateTT():
    display = Display()
    display.print_available_data()
    genrationNumber = 0
    print("\n> Generation # " + str(genrationNumber))
    population = Population(POPULATION_SIZE)  # awl random generation

    population.get_schedules().sort(key=get_sort_key, reverse=True)  # higher fitness & less no. of conflicts foooooo2
    # display.print_generation(population)
    genatic = genatic_algorithm()

    while (population.get_schedules()[0].get_fitness() != 1.0):
        genrationNumber += 1
        print("\n> Generation # " + str(genrationNumber))
        population = genatic.evolve(population)
        population.get_schedules().sort(key=get_sort_key, reverse=True)  # reverse 34an by sort 7sb elfitness
        display.print_generation(population)

    print("\n\n")
    display.print_schedule_as_table(population.get_schedules()[0])
    return display.save_schedule_as_model(population.get_schedules()[0])

def get_timeslots():
    display = Display()
    return display.get_Time_slots()


