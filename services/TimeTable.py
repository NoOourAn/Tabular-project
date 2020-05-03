import prettytable as prettytable
from random import randint
from random import random
from datetime import datetime
import services.dbconvert as ma3lomat

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


class Data:#[id, "start - end", day, daynum]
    Time_Avilable = [[1, "09:00 - 10:00", "SUNDAY", "1/1"],
                     [2, "10:00 - 11:00", "SUNDAY", "1/1"],
                     [3 , "11:00 - 12:00", "SUNDAY", "1/1"],
                     [4 , "09:00 - 10:00", "SUNDAY", "8/1"],
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

    print("dat")
    def __init__(self):
        print("dataaaaaa")
        excel = ma3lomat.fetch_data()
        print("adadadaddada")
        self.ROOMS = excel.fetch_rooms_data()
        self.cat = excel.fetch_students_data()    # course:course-info (name-ins-....)
        self.co =excel.fetch_subjects_data()    # course:students
        self.d = excel.fetch_dept_data()
        self._rooms = []
        self._TimeAvilable = []
        self._instructors = []
        self._students = []

        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.Time_Avilable)):
            self._TimeAvilable.append(TimeAvilable(self.Time_Avilable[i][0], self.Time_Avilable[i][1], self.Time_Avilable[i][2] ,self.Time_Avilable[i][3]))
        # for i in range(0, len(self.INSTRUCTORS)):
        #     self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        # for i in range(0, len(self.STUDENT)):
        #     self._students.append(Student(self.STUDENT[i][0], self.STUDENT[i][1], self.STUDENT[i][2]))
        # if self.STUDENT[i][2] in self._studentcategory:
        #     stu = self._studentcategory[self.STUDENT[i][2]]
        #     self._studentcategory[self.STUDENT[i][2]] = stu + self.STUDENT[i][1]
        # else:
        #     self._studentcategory[self.STUDENT[i][2]] =  self.STUDENT[i][1]

        courses_list = []
        id = 0
        for key in self.co:
            for key2 in self.cat:

                if self.co[key][0] == key2:
                    self._instructors.append(Instructor(id, self.co[key][1]))
                    coursee = Courses(key, self.co[key][0], [self._instructors[id]], self.cat[key2],
                    self.co[key][3])
                    courses_list.append(coursee)
                    id = id + 1
        self._courses = courses_list

        deptlist = []
        for key in self.d:
            d = []
            for i in self._courses:
                if i.get_name() in self.d[key]:
                    d.append(i)
            deptt = Department(key, d)
            deptlist.append(deptt)
        self.depts = deptlist
        self.numberOfClasses = 0
        self.numberOfClasses = len(self._courses)

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
        self.data = Data()  # used in schedule class
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
                new_exam.set_TimeAvilable(self.data.get_TimeAvilable()[randint(0, len(self.data.get_TimeAvilable()) - 1)])
                new_exam.set_room(self.data.get_rooms()[randint(0, len(self.data.get_rooms()) - 1)])
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
        self.schedules = []
        for i in range(0, size):
            self.schedules.append(schedule().initialize())   # bycreate el popu mn class schedule
    def get_schedules(self):
        return self.schedules


############################## L7d hena done ^_^
class genatic_algorithm:
    POPULATION_SIZE = 10
    NUMB_OFELITE_SCHEDULES = 1  ####
    TORNAMENT_SELECTON_SIZE = 2  ####  no of parents
    MUTATION_RATE = 0.1  ####

    def evolve(self, popu):  # de bs elly bst5dmha direct fe el main w hia btst5dm elly t7tha
        return self.mutation(self.crossover(popu))

    def crossover(self, popu):
        crossover_pop = Population(0)
        for i in range(self.NUMB_OFELITE_SCHEDULES):
            crossover_pop.get_schedules().append(
                popu.get_schedules()[i])  # take a copy of population list not reference(only the last 9)
        # i = NUMB_OFELITE_SCHEDULES
        i = 0
        while i < self.POPULATION_SIZE:
            schedule1 = self.select_tournament_population(popu).get_schedules()[0]
            schedule2 = self.select_tournament_population(popu).get_schedules()[1]
            crossover_pop.get_schedules().append(self.crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def mutation(self, popu):  # mutate every schedule in population
        for i in range(0, self.POPULATION_SIZE):  # NUMB_OFELITE_SCHEDULES
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
            if (self.MUTATION_RATE > random()):
                mutate.get_exams()[i] = scheduler.get_exams()[i]
        return mutate

    def select_tournament_population(self, popu):  # to select parents
        tournament_pop = Population(0)
        i = 0
        while i < self.TORNAMENT_SELECTON_SIZE:
            tournament_pop.get_schedules().append(popu.get_schedules()[randint(0, self.POPULATION_SIZE - 1)])
            i += 1
        tournament_pop.get_schedules().sort(key=get_sort_key, reverse=True)
        return tournament_pop


class Display:
    def __init__(self):
        self.data = Data()
    def print_available_data(self):
        print("> ALL Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_Time_Avilable()

    def print_dept(self):
        depts = self.data.get_depts()
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
        courses = self.data.get_courses()
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
        # data = Data()
        availableInstructorsTable = prettytable.PrettyTable(['id', 'instructors'])
        instructors = self.data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])

        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = self.data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)

    def print_Time_Avilable(self):
        availableTimeAvilableTable = prettytable.PrettyTable(['id', 'Time', 'day', 'date'])
        timeAvilable = self.data.get_TimeAvilable()
        for i in range(0, len(timeAvilable)):
            availableTimeAvilableTable.add_row([timeAvilable[i].get_id(), timeAvilable[i].get_time(), timeAvilable[i].get_day() , timeAvilable[i].get_date()])
        print(availableTimeAvilableTable)

    def get_Time_slots(self):
        timeslots = []
        timeAvilable = self.data.get_TimeAvilable()
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


def get_sort_key(list):
    return list.get_fitness()  # de func mwgoda fe class schedule

def sort_by_id(exams):
    return datetime.strptime(exams[3], "%d/%m")

def generateTT():
    POPULATION_SIZE = 10
    display = Display()
    display.print_available_data()
    genrationNumber = 0
    print("\n> Generation # " + str(genrationNumber))
    population = Population(POPULATION_SIZE)  # awl random generation  --- awl nadha LL data

    population.get_schedules().sort(key=get_sort_key, reverse=True)  # higher fitness & less no. of conflicts foooooo2
    display.print_generation(population)
    genatic = genatic_algorithm()

    while (population.get_schedules()[0].get_fitness() != 1.0):
        genrationNumber += 1
        print("\n> Generation # " + str(genrationNumber))
        population = genatic.evolve(population)
        population.get_schedules().sort(key=get_sort_key, reverse=True)  # reverse 34an by sort 7sb elfitness
        # display.print_generation(population)

    print("\n\n")
    display.print_schedule_as_table(population.get_schedules()[0])
    return display.save_schedule_as_model(population.get_schedules()[0])

def get_timeslots():
    display = Display()
    return display.get_Time_slots()

