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
        # loc = self.assign.get_StudentsFilename()
        # wb = xlrd.open_workbook(loc, on_demand=True)
        wb = self.assign.get_StudentsFilename()
        if wb !=  None:
            sheets = wb.sheetnames
            print(sheets)
            # sheet = wb.sheet_by_index(0)
            # sheet.cell_value(0, 0)
            # maxofstudent = my_dictionary()
            sheet = wb["Sheet1"]
            # for i in range(sheet.nrows):
            #     count = 0
            #     subjects =sheet.cell_value(i, 0)
            #     students= sheet.row_values(i,1)
            #     dict_obj.add_cat(subjects,students)
            i = 1
            for row in sheet.iter_rows(values_only=True):
                subjects = sheet.cell(row=i, column=1)
                students = []
                for col in sheet.iter_cols(min_col=2, values_only=True):
                    for cell in col:
                        students.append(cell)
                dict_obj.add_cat(subjects,students)
                i = i+1
            # wb.release_resources()
        return dict_obj
    #     print(students[i])
    #     while students[i] == '' :
    #         continue
    #     maxofstudent.add_cat(subjects,len(students))
    #

    def fetch_rooms_data(self):
        # loc2 = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVROOMSDATASET.xlsx')  #rooms
        # listoflists = []
        excel_data = []

        # loc2 = self.assign.get_RoomsFilename()
        # wb2 = xlrd.open_workbook(loc2, on_demand=True)
        wb = self.assign.get_RoomsFilename()
        if wb != "":
            # sheet2 = wb2.sheet_by_index(0)
            worksheet = wb["Sheet1"]
            # worksheet.cell_value(0, 0)
            # for i in range(worksheet.nrows):
            #     sublist = []
            #     rooms = worksheet.cell_value(i, 0)
            #     capacity = worksheet.cell_value(i, 1)
            #     sublist.append(rooms)
            #     sublist.append(capacity)
            #     listoflists.append(sublist)

            for row in worksheet.iter_rows():
                row_data = []
                for cell in row:
                    row_data.append(str(cell.value))    #feha 7aga 8lt
                excel_data.append(row_data)

            # wb2.release_resources()
        return excel_data

    def fetch_subjects_data(self):
        # loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/C.xlsx') #courses
        listfadia = []
        dict_obj2 = my_dictionary()
        # loc = self.assign.get_SubjectsFilename()
        # wb = xlrd.open_workbook(loc, on_demand=True)
        wb = self.assign.get_SubjectsFilename()
        if wb != None:
            # sheet = wb.sheet_by_index(0)
            sheet = wb["Sheet1"]
            # sheet = wb.active
            # sheet.cell_value(0, 0)
            # for i in range(sheet.nrows):
            #     subjects =sheet.cell_value(i, 0)
            #     j=1
            #     students= sheet.row_values(i,j)
            #     dict_obj2.add_cat(subjects,students)

            i = 1
            for row in sheet.iter_rows(values_only=True):
                subjects = sheet.cell(row=i, column=1)
                students = []
                for col in sheet.iter_cols(min_col=2, values_only=True):
                    for cell in col:
                        students.append(cell)
                dict_obj2.add_cat(subjects,students)
                i = i+1

            for key in dict_obj2 :
                self.testdept.add_cat(dict_obj2[key][2],listfadia)
            for x in self.testdept:
                l = []
                for key in dict_obj2:
                    if x == dict_obj2[key][2]:
                        l.append(dict_obj2[key][0])
                self.testdept[x]=l
            # wb.release_resources()
        return dict_obj2

    def fetch_dept_data(self):
        return self.testdept




