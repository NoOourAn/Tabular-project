import xlrd

# from services.views import assign


class my_dictionary(dict):
    def __init__(self):
        self=dict()

    def add_cat(self, key , value):
        self[key]= value


class assign_data:
    def __init__(self):
        self._StudentsFile = None
        self._SubjectsFile = None
        self._RoomsFile = None
        self._Timeslots = []


    def get_StudentsFile(self):return self._StudentsFile
    def set_StudentsFile(self, file): self._StudentsFile = file

    def get_SubjectsFile(self):return self._SubjectsFile
    def set_SubjectsFile(self, file): self._SubjectsFile = file

    def get_RoomsFile(self):return self._RoomsFile
    def set_RoomsFile(self, file): self._RoomsFile = file

    def get_TimeSlots(self):return self._Timeslots
    def set_TimeSlots(self, timeslots): self._Timeslots = timeslots


class fetch_data:
    assign = assign_data()
    testdept = my_dictionary()
    def fetch_students_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVDATASET.xlsx')  #cat
        courses_data_students = my_dictionary()
        wb = self.assign.get_StudentsFile()
        if wb !=  None:
            sheet = wb["Sheet1"]
            i = 1
            for row in sheet.iter_rows( values_only=True):
                subjects = sheet.cell(row=i, column=1)
                students = []
                j = 2
                for cell in row:
                    temp = sheet.cell(row=i, column=j)
                    students.append(temp.value)
                    j = j + 1
                courses_data_students.add_cat(subjects.value, students)
                i = i + 1
        return courses_data_students

    def fetch_rooms_data(self):
        # loc2 = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVROOMSDATASET.xlsx')  #rooms
        rooms_capacity = []
        wb = self.assign.get_RoomsFile()
        if wb != None:
            worksheet = wb["Sheet1"]
            for row in worksheet.iter_rows():
                row_data = []
                for cell in row:
                    row_data.append(cell.value)    #h333 s77
                rooms_capacity.append(row_data)
        return rooms_capacity

    def fetch_subjects_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/C.xlsx') #courses_data
        info = []
        courses_data = my_dictionary()
        wb = self.assign.get_SubjectsFile()
        if wb != None:
            sheet = wb["Sheet1"]
            i = 1
            for row in sheet.iter_rows(max_col=4,values_only=True):
                subjects = sheet.cell(row=i, column=1)
                students = []
                j = 2
                for col in sheet.iter_cols(max_col=4,values_only=True):
                    temp = sheet.cell(row=i,column=j)
                    students.append(temp.value)
                    j=j+1
                courses_data.add_cat(subjects.value, students)
                i = i+1
            # print(courses_data)
            for key in courses_data :
                self.testdept.add_cat(courses_data[key][2],info)
            for x in self.testdept:
                l = []
                for key in courses_data:
                    if x == courses_data[key][2]:
                        l.append(courses_data[key][0])
                self.testdept[x]=l
        return courses_data

    def fetch_dept_data(self):
        return self.testdept

    def fetch_time_data(self):
        timeslots = self.assign.get_TimeSlots()
        return timeslots


