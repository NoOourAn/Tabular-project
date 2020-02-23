# import pandas as pd
#
#
# data = pd.read_excel (r'C:\Users\Ahmed_ELSami\Desktop\MINI UNIV DATASET.xlsx')
#
# df = pd.DataFrame(data, columns[0])
#
# print (df)
###################################################################################

# Program extracting first column

import xlrd


class my_dictionary(dict):
    def __init__(self):
        self=dict()

    def add(self, key , value):
        self[key]= value



loc = ('C:/Users/Ahmed_ELSami/Desktop/MINIUNIVDATASET.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
dict_obj = my_dictionary()





for i in range(sheet.nrows):

    subjects =sheet.cell_value(i, 0)

   # print(subjects)

    students= sheet.row_values(i)
    #print(students)

    dict_obj.add(subjects,students)


# print(subjects)
# print(students)

print(dict_obj)



# StudentOnly = students - subjects
#
# print(StudentOnly)

print(dict)