import random,xlrd,xlwt,sys,os
from os import path
address = sys.argv[1]
address = sys.argv[1].replace('\\','\\\\')
dict_age_out = {}
dict_class_out = {}
dict_name_out = {}
def load_int_excel(row,address):
    data = xlrd.open_workbook(address)
    table = data.sheets()[0]
    nor = table.nrows
    nol = table.ncols
    dict = {}
    for i in range(1, nor):
        order = int(table.cell_value(i, 0))
        value = table.cell_value(i, row)
        dict[order] = int(value)
    return dict
def load_str_excel(row,address):
    data = xlrd.open_workbook(address)
    table = data.sheets()[0]
    nor = table.nrows
    nol = table.ncols
    dict = {}
    for i in range(1, nor):
        order = int(table.cell_value(i, 0))
        value = table.cell_value(i, row)
        dict[order] = value
    return dict
def dynamic_arrary(number):
    arrary = []
    for i in range(1,number+1):
        arrary.append(i)
    return arrary
def random_pool(number, dict_age, dict_init1, dict_init2, dict_init3):
    temp = []
    for i in range(number):
        a = random.randint(1, len(dict_age))
        for p in range(len(temp)):
            while (a == temp[p]):
                a = random.randint(1, len(dict_age))
        temp.append(a)
    temp2 = []
    for t in range(len(temp)):
        for s in range(len(temp)):
            if (t != s) & (temp[t] == temp[s]) & ~(t in temp2) & ~(s in temp2):
                temp2.append(t)
                temp2.append(s)
    for w in range(len(temp2)):
        for g in range(number):
            if (g != 0) & ~(g in temp):
                temp[temp2[w]] = g
    for w in range(number):
        dict_init1[w+ 1]= dict_age[temp[w]]
        dict_init2[w+ 1] = dict_class[temp[w]]
        dict_init3[w+ 1] = dict_name[temp[w]]
def dynamic_judge_age(class_number, people_sum ,dict_init):
    judge_single = True
    for i in range(class_number-1):
        judge_single = judge_single & ((dict_init[((people_sum * i) / class_number) + 1] - dict_init[(people_sum/class_number)*(i + 1)]) > (((max(dict_init) - min(dict_init)) / len(dict_init))) * (people_sum / class_number -1))
    return judge_single
def dynamic_judge_class(class_number,people_sum,dict_init ):
    judge_single1 = True
    for i in range(class_number - 1):
        for t in range((int((people_sum * i) / class_number) + 1),int((people_sum/class_number)*(i + 1))):
            judge_single1 = judge_single1 & ((dict_init[t] != dict_init[random.randint(((people_sum * i) / class_number) + 1,(people_sum/class_number)*(i + 1))] ))
    return judge_single1
def out_excel(adress,number):
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('0')
    worksheet.write(0,0,'序号')
    worksheet.write(0,1,'姓名')
    worksheet.write(0,2,'年龄')
    worksheet.write(0,3,'实验室')
    for i in dynamic_arrary(number):
        worksheet.write(i,0,i)
        worksheet.write(i,1,dict_name_out[i])
        worksheet.write(i,2,dict_age_out[i])
        worksheet.write(i,3,dict_class_out[i])
    workbook.save(adress)
dict_age = load_int_excel(2,address)
dict_class = load_int_excel(3,address)
dict_name = load_str_excel(1,address)
people_number = len(dict_age)
group_number = int(input('输入分的小组数并回车：'))
random_pool(people_number,dict_age,dict_age_out,dict_class_out,dict_name_out)
while not((dynamic_judge_age(group_number,people_number,dict_age_out)) & dynamic_judge_class(group_number,people_number,dict_class_out)):
    random_pool(people_number,dict_age,dict_age_out,dict_class_out,dict_name_out)
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_excel(pwd + '\\\\randomlist.xls',people_number)
print(dict_age_out)
print(dict_class_out)
print(dict_name_out)

os.system("pause")