import prettytable as prettytable
from  random import randint
from  random import random
from ..services.models import Timetables

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
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def get_id(self): return self.id

    def get_time(self): return self.time
class Courses:
    def __init__(self, number, name, instructors, students, maxNumbOfStudents):   #maxnumber htb2a len(students)
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
    ROOMS = [["R1", 25], ["R2", 45], ["R3", 35],["R4", 25],["R5", 45],["R6", 35],["R7", 25],["R8", 45],["R9", 45],["R10", 35]]
    Time_Avilable = [["TimeSlot-1", "Mon 09:00 - 10:00"],
                     ["TimeSlot-2", "Mon 10:00 - 11:00"],
                     ["TimeSlot-3", "Wed 09:00 - 10:30"],
                     ["TimeSlot-4", "Wed 10:30 - 12:00"],
                     ["TimeSlot-5", "Thu 09:00 - 10:00"],
                     ["TimeSlot-6", "Thu 10:00 - 11:00"],
                     ["TimeSlot-7", "Sun 09:00 - 10:00"],
                     ["TimeSlot-8", "Sun 10:00 - 11:00"],
                     ["TimeSlot-9", "Tue 09:00 - 10:00"],
                     ["TimeSlot-10", "Tue 10:00 - 11:00"]]
    INSTRUCTORS = [["id-1", "DR Gean"],
                       ["id-2", "DR James"],
                       ["id-3", "Mr Mike"],
                       ["id-4", "DR Steve"]]
    STUDENT = [["id-1", "nour" , "mm ir"],
                   ["id-2", "kera" , "mm ir"],
                   ["id-3", "simba" , "ds logic"],
                   ["id-4", "Limo", "or pat"],
                   ["id-5", "neer", "ds logic"],
                   ["id-6", "shimngi", "pl logic"]]


    cat = {"mm":["nour","kera","x","m"] ,
           "ir":["nour","kera"] ,
           "ds":["simba","neer"],
           "logic":["neer","shimngi"] ,
           "or":["Limo","x"],
           "pat": ["Limo","x","kera"],
           "cs":["simba","neer","shimngi"],
           "is":["simba","neer","shimngi"],
           "math1":["nour","simba","neer","shimngi"],
           "eng1":["shimngi","kera"],
           "phy":["neer","L","kera"],
           "elec":["shimngi","L"],
           "econ":["neer","shimngi","L","kera"],
           "it":["simba","neer","x","m"],
           "math2":["nour","x","m"],
           "stat":["nour","x","m"],
           "eng2":["nour","Limo","x","m"],
           "pl":["Limo","m"],
           "algo":["L","Limo"],
           "hr":["simba","L","Limo"],
           "db1":["simba","L"],
           "pl2":["L","m"]}

    def __init__(self):
        self._rooms = []
        self._TimeAvilable = []
        self._instructors = []
        self._students = []
        # self._studentcategory = {}

        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.Time_Avilable)):
            self._TimeAvilable.append(TimeAvilable(self.Time_Avilable[i][0], self.Time_Avilable[i][1]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        for i in range(0, len(self.STUDENT)):
            self._students.append(Student(self.STUDENT[i][0], self.STUDENT[i][1], self.STUDENT[i][2]))
            # if self.STUDENT[i][2] in self._studentcategory:
            #     stu = self._studentcategory[self.STUDENT[i][2]]
            #     self._studentcategory[self.STUDENT[i][2]] = stu + self.STUDENT[i][1]
            # else:
            #     self._studentcategory[self.STUDENT[i][2]] =  self.STUDENT[i][1]
        course1 = Courses("C1", "mm", [self._instructors[0], self._instructors[1]],self.cat["mm"], 25)  #(number, name, instructors,students, maxNumbOfStudents)
        course2 = Courses("C2", "pl", [self._instructors[0], self._instructors[1], self._instructors[2]],self.cat["pl"], 35)
        course3 = Courses("C3", "ir", [self._instructors[0], self._instructors[1]],self.cat["ir"] ,25)
        course4 = Courses("C4", "or", [self._instructors[2], self._instructors[3]],self.cat["or"] ,30)
        course5 = Courses("C5", "ds", [self._instructors[3]], self.cat["ds"],35)
        course6 = Courses("C6", "logic", [self._instructors[0], self._instructors[2]],self.cat["logic"] ,45)
        course7 = Courses("C7", "pat", [self._instructors[1], self._instructors[3]], self.cat["pat"],45)
        course8 = Courses("C8", "cs", [self._instructors[2], self._instructors[3]], self.cat["cs"],30)
        course9 = Courses("C9", "is", [self._instructors[1], self._instructors[3]], self.cat["is"],35)
        course10 = Courses("C10", "math1", [self._instructors[1], self._instructors[3]], self.cat["math1"],45)
        course11 = Courses("C11", "eng1", [self._instructors[2], self._instructors[3]], self.cat["eng1"],35)
        course12 = Courses("C12", "elec", [self._instructors[0], self._instructors[1], self._instructors[2]], self.cat["elec"],35)
        course13 = Courses("C13", "phy", [self._instructors[1], self._instructors[3]], self.cat["phy"],35)
        course14 = Courses("C14", "econ", [self._instructors[2], self._instructors[3]], self.cat["econ"],35)
        course15 = Courses("C15", "it", [self._instructors[0], self._instructors[1], self._instructors[2]], self.cat["it"],35)
        course16 = Courses("C16", "math2", [self._instructors[1], self._instructors[3]], self.cat["math2"],35)
        course17 = Courses("C17", "algo", [self._instructors[3]], self.cat["algo"],45)
        course18 = Courses("C18", "stat", [self._instructors[2], self._instructors[3]], self.cat["stat"],45)
        course19 = Courses("C19", "eng2", [self._instructors[1], self._instructors[3]], self.cat["eng2"],25)
        course20 = Courses("C20", "db1", [self._instructors[2], self._instructors[3]], self.cat["db1"],25)
        course21 = Courses("C21", "hr", [self._instructors[2], self._instructors[3]], self.cat["hr"],25)
        course22 = Courses("C22", "pl2", [self._instructors[0], self._instructors[1], self._instructors[2]], self.cat["pl2"],25)

        self._courses = [course1, course2, course3, course4, course5, course6, course7, course8, course9, course10,
            course11, course12, course13, course14, course15, course16, course17, course18, course19, course20, course21, course22]
        dept1 = Department("Cs", [course1, course3, course8, course9, course16, course17, course22])
        dept2 = Department("Is", [course2, course4, course5, course10,course14, course15, course18, course19])
        dept3 = Department("It", [course6, course7,course11, course12, course13, course20, course21])
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
    def __init__(self, id, dept, course,students):
        self._id = id
        self._dept = dept
        self._course = course
        self._students = students
        #the rest will be assigned random
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

    #to be set random
    def set_instructor(self, instructor): self._instructor = instructor
    def set_TimeAvilable(self, TimeAvilable): self._TimeAvilable = TimeAvilable
    def set_room(self, room): self._room = room

    def __str__(self):          #used in display class
        return "{" + str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(
            self._TimeAvilable.get_id()) + "," + str(len(self._students)) + "}"
class schedule:
    def __init__(self):
        self.data = data
        self.exams = []         #of the schedule instances
        self.num_of_conflict = 0
        self.fitness = -1
        self.examcounter = 0      #counter to use in the initialization func
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
    def get_exams(self):        #mohema fe class GA
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
                    if (exams[i].get_TimeAvilable() == exams[j].get_TimeAvilable() and exams[i].get_id() != exams[j].get_id()):
                        if (exams[i].get_room() == exams[j].get_room()): self.num_of_conflict += 1
                        # if (exams[i].get_instructor() == exams[j].get_instructor()): self.num_of_conflict += 1
                    #lists of students need to be alphabetically ordered
                        if (not set(exams[i].get_students()).isdisjoint(exams[j].get_students())): self.num_of_conflict += 1
                        # if (classes[i].get_students() == classes[j].get_students()): self.num_of_conflict += 1
        return 1 / ((1.0 * self.num_of_conflict)+1)  # *1.0 to convert int to float
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
        self.data = data             #mlhaaa4 lazma t2rebn
        self.schedules = []
        for i in range(0, size):
            self.schedules.append(schedule().initialize())

    def get_schedules(self):
        return self.schedules
############################## L7d hena done ^_^
class genatic_algorithm:

    def evolve(self, popu):         #de bs elly bst5dmha direct fe el main w hia btst5dm elly t7tha
        return self.mutation(self.crossover(popu))

    def crossover(self, popu):
        crossover_pop = Population(0)
        for i in range(NUMB_OFELITE_SCHEDULES):
            crossover_pop.get_schedules().append(popu.get_schedules()[i])  # take a copy of population list not reference
        # i = NUMB_OFELITE_SCHEDULES
        i = 0
        while i < POPULATION_SIZE:
            schedule1 = self.select_tournament_population(popu).get_schedules()[0]
            schedule2 = self.select_tournament_population(popu).get_schedules()[1]
            crossover_pop.get_schedules().append(self.crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def mutation(self, popu):  #mutate every schedule in population
        for i in range(NUMB_OFELITE_SCHEDULES, POPULATION_SIZE):
            self.mutate_schedule(popu.get_schedules()[i])
        return popu

    def crossover_schedule(self, schedule1, schedule2):  #get new childe from restored  2 schduler parent
        crossoverSchedule = schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_exams())):
            if (random() > 0.5):
                crossoverSchedule.get_exams()[i] = schedule1.get_exams()[i]
            else:
                crossoverSchedule.get_exams()[i] = schedule2.get_exams()[i]
        return crossoverSchedule

    def mutate_schedule(self, mutate):   # mutate 1 schedule
        scheduler = schedule().initialize()
        for i in range(0, len(mutate.get_exams())):
            if (MUTATION_RATE > random()):
                mutate.get_exams()[i] = scheduler.get_exams()[i]
        return mutate

    def select_tournament_population(self, popu):  # to select parents
        tournament_pop = Population(0)
        i = 0
        while i < TORNAMENT_SELECTON_SIZE:
            tournament_pop.get_schedules().append(popu.get_schedules()[randint(0, POPULATION_SIZE -1)])
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
        availableTimeAvilableTable = prettytable.PrettyTable(['id', 'Time Avilable'])
        timeAvilable = data.get_TimeAvilable()
        for i in range(0, len(timeAvilable)):
            availableTimeAvilableTable.add_row([timeAvilable[i].get_id(), timeAvilable[i].get_time()])
        print(availableTimeAvilableTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            ['schedule #', 'fitness', '# of conflicts', 'classes[dept,course,room,instructor,no of students]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_number_Of_conflict(), schedules[i]])
        print(table1)

    def print_schedule_as_table(self, schedule):
        tt = Timetables()
        classes = schedule.get_exams()
        table = prettytable.PrettyTable(
            ['Exam #', 'Dept', 'Course(number , max # of students)', 'Room (Capacity)', 'Instructor','TimeAvilable'])
        for i in range(0, len(classes)):
            table.add_row([str(i), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " + str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_seatingCapacity())+")",
                           classes[i].get_instructor().get_name() + " (" + str(classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_TimeAvilable().get_time() + " (" + str(classes[i].get_TimeAvilable().get_id()) + ")"])

            tt.exams += classes[i].get_course().get_number() + ", " + classes[i].get_room().get_number() + ", " + + str(classes[i].get_TimeAvilable().get_id())

        tt.accessCode = 'traaa5'
        tt.save()
        print(table)

POPULATION_SIZE = 10
NUMB_OFELITE_SCHEDULES = 1         ####
TORNAMENT_SELECTON_SIZE = 2         ####  no of parents
MUTATION_RATE = 0.1                 ####

data = Data()    #used in schedule class
display = Display()
display.print_available_data()

genrationNumber = 0
print("\n> Generation # " + str(genrationNumber))
population = Population(POPULATION_SIZE)        #awl random generation
def get_sort_key(list):
    return list.get_fitness()      #de func mwgoda fe class schedule

population.get_schedules().sort(key=get_sort_key, reverse=True)       #higher fitness & less no. of conflicts foooooo2
display.print_generation(population)
genatic=genatic_algorithm()

while (population.get_schedules()[0].get_fitness() != 1.0):
    genrationNumber += 1
    print("\n> Generation # " + str(genrationNumber))
    population = genatic.evolve(population)
    population.get_schedules().sort(key=get_sort_key, reverse=True)    #reverse 34an by sort 7sb elfitness
    display.print_generation(population)

print("\n\n")
display.print_schedule_as_table(population.get_schedules()[0])

