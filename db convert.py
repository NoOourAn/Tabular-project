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

class my_list(list):
    def __init__(self):
        self=list()

    def add(self, value1 , value2):
        list1=list.append(self,value1)
        list2=list.append(self,value2)
        # self=list1.append(list2)
        # li =[]
        for i in list1,list2:
            self[i] = list1[i]+list2[i]



loc = ('C:/Users/Ahmed_ELSami/Desktop/MINIUNIVDATASET.xlsx')  #cat

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
dict_obj = my_dictionary()

for i in range(sheet.nrows):

    subjects =sheet.cell_value(i, 0)
   # print(subjects)
    j=1
    students= sheet.row_values(i,j)
    #print(students)

    dict_obj.add(subjects,students)
# print(subjects)
# print(students)
print(dict_obj)
#print(dict)

loc2 = ('C:/Users/Ahmed_ELSami/Desktop/MINIUNIVROOMSDATASET.xlsx')  #rooms

wb2 = xlrd.open_workbook(loc2)
sheet2 = wb2.sheet_by_index(0)
sheet2.cell_value(0, 0)
dict_obj2 = my_dictionary()
list_obj= my_list()


for i in range(sheet2.nrows):
    rooms = list(sheet2.cell_value(i, 0))
    #print(rooms)
    capacity = list(sheet2.row_values(i,1))
    #print(capacity)
    rooms.append(capacity)
list_obj= my_list()
list_obj.add(rooms,capacity)
print(list_obj)



