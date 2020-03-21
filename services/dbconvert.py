import xlrd

class my_dictionary(dict):
    def __init__(self):
        self=dict()

    def add_cat(self, key , value):
        self[key]= value

    # def add_course(self, key , v1, v2):
    #     self[key]= {'v1' , 'v2'}



loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVDATASET.xlsx')  #cat

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
dict_obj = my_dictionary()
maxofstudent = my_dictionary()

for i in range(sheet.nrows):

    count = 0
    subjects =sheet.cell_value(i, 0)
    students= sheet.row_values(i,1)
    dict_obj.add_cat(subjects,students)
#     print(students[i])
#     while students[i] == '' :
#         continue
#     maxofstudent.add_cat(subjects,len(students))
#
# print(maxofstudent)
print(dict_obj)


loc2 = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/MINIUNIVROOMSDATASET.xlsx')  #rooms

wb2 = xlrd.open_workbook(loc2)
sheet2 = wb2.sheet_by_index(0)
sheet2.cell_value(0, 0)

listoflists = []

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
print(listoflists)

loc = ('C:/Users/NoURan/Desktop/Tabular-project/services/excel/C.xlsx') #courses
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
dict_obj2 = my_dictionary()
testdept= my_dictionary()
listfadia = []

for i in range(sheet.nrows):

    subjects =sheet.cell_value(i, 0)
    j=1
    students= sheet.row_values(i,j)
    dict_obj2.add_cat(subjects,students)

print(dict_obj2)

for key in dict_obj2 :
    testdept.add_cat(dict_obj2[key][2],listfadia)



# l = []

for x in testdept:
    l = []
    for key in dict_obj2:
        if x == dict_obj2[key][2]:
            l.append(dict_obj2[key][0])
    testdept[x]=l


print(testdept)



