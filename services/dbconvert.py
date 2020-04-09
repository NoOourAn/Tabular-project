import xlrd

# from services.views import assign


class my_dictionary(dict):
    def __init__(self):
        self=dict()

    def add_cat(self, key , value):
        self[key]= value

    # def add_course(self, key , v1, v2):
    #     self[key]= {'v1' , 'v2'}

class assign_filename:
    def __init__(self):
        self._StudentsFilename = ""
        self._SubjectsFilename = ""
        self._RoomsFilename = ""

    def get_StudentsFilename(self):return self._StudentsFilename
    def set_StudentsFilename(self, filename): self._StudentsFilename = filename

    def get_SubjectsFilename(self):return self._SubjectsFilename
    def set_SubjectsFilename(self, filename): self._SubjectsFilename = filename

    def get_RoomsFilename(self):return self._RoomsFilename
    def set_RoomsFilename(self, filename): self._RoomsFilename = filename


class fetch_data:
    assign = assign_filename()
    testdept = my_dictionary()
    def fetch_subjects_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVDATASET.xlsx')  #cat
        dict_obj = my_dictionary()
        loc = self.assign.get_StudentsFilename()
        if loc != "":
            wb = xlrd.open_workbook(loc ,on_demand = True)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            # maxofstudent = my_dictionary()

            for i in range(sheet.nrows):
                count = 0
                subjects =sheet.cell_value(i, 0)
                students= sheet.row_values(i,1)
                dict_obj.add_cat(subjects,students)
            wb.release_resources()
        return dict_obj
    #     print(students[i])
    #     while students[i] == '' :
    #         continue
    #     maxofstudent.add_cat(subjects,len(students))
    #

    def fetch_rooms_data(self):
        # loc2 = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVROOMSDATASET.xlsx')  #rooms
        listoflists = []
        loc2 = self.assign.get_RoomsFilename()
        if loc2 != "":
            wb2 = xlrd.open_workbook(loc2 ,on_demand = True)
            sheet2 = wb2.sheet_by_index(0)
            sheet2.cell_value(0, 0)
            for i in range(sheet2.nrows):
                sublist = []
                rooms = sheet2.cell_value(i, 0)
                #print(rooms)
                # capacity = sheet2.row_values(i,1)
                capacity = sheet2.cell_value(i, 1)
                #print(capacity)
                # sublist.append((rooms, capacity))
                sublist.append(rooms)
                sublist.append(capacity)
                listoflists.append(sublist)
            wb2.release_resources()
        return listoflists

    def fetch_students_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/C.xlsx') #courses
        listfadia = []
        dict_obj2 = my_dictionary()
        loc = self.assign.get_SubjectsFilename()
        if loc != "":
            wb = xlrd.open_workbook(loc,on_demand = True)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            for i in range(sheet.nrows):
                subjects =sheet.cell_value(i, 0)
                j=1
                students= sheet.row_values(i,j)
                dict_obj2.add_cat(subjects,students)
            for key in dict_obj2 :
                self.testdept.add_cat(dict_obj2[key][2],listfadia)
            for x in self.testdept:
                l = []
                for key in dict_obj2:
                    if x == dict_obj2[key][2]:
                        l.append(dict_obj2[key][0])
                self.testdept[x]=l
            wb.release_resources()
        return dict_obj2

    def fetch_dept_data(self):
        return self.testdept




