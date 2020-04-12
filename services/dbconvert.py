import xlrd

# from services.views import assign


class my_dictionary(dict):
    def __init__(self):
        self=dict()

    def add_cat(self, key , value):
        self[key]= value


class assign_filename:
    def __init__(self):
        self._StudentsFilename = None
        self._SubjectsFilename = None
        self._RoomsFilename = None

    def get_StudentsFilename(self):return self._StudentsFilename
    def set_StudentsFilename(self, filename): self._StudentsFilename = filename

    def get_SubjectsFilename(self):return self._SubjectsFilename
    def set_SubjectsFilename(self, filename): self._SubjectsFilename = filename

    def get_RoomsFilename(self):return self._RoomsFilename
    def set_RoomsFilename(self, filename): self._RoomsFilename = filename


class fetch_data:
    assign = assign_filename()
    testdept = my_dictionary()
    def fetch_students_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVDATASET.xlsx')  #cat
        dict_obj = my_dictionary()
        wb = self.assign.get_StudentsFilename()
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
                dict_obj.add_cat(subjects.value, students)
                i = i + 1
        return dict_obj

    def fetch_rooms_data(self):
        # loc2 = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVROOMSDATASET.xlsx')  #rooms
        excel_data = []
        wb = self.assign.get_RoomsFilename()
        if wb != None:
            worksheet = wb["Sheet1"]
            for row in worksheet.iter_rows():
                row_data = []
                for cell in row:
                    row_data.append(cell.value)    #h333 s77
                excel_data.append(row_data)
        return excel_data

    def fetch_subjects_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/C.xlsx') #courses
        listfadia = []
        dict_obj2 = my_dictionary()
        wb = self.assign.get_SubjectsFilename()
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
                dict_obj2.add_cat(subjects.value, students)
                i = i+1
            print(dict_obj2)
            for key in dict_obj2 :
                self.testdept.add_cat(dict_obj2[key][2],listfadia)
            for x in self.testdept:
                l = []
                for key in dict_obj2:
                    if x == dict_obj2[key][2]:
                        l.append(dict_obj2[key][0])
                self.testdept[x]=l
        return dict_obj2

    def fetch_dept_data(self):
        return self.testdept




