from csv import DictReader
from json import load
from employee import *


#ЕСЛИ ДОЛЖНОСТИ НЕТ - УДАЛЯТЬ!


input_name = '../Temp/fi3.txt'
output_name = '../Temp/fo.csv'
delim = '\t'
# yo_check = False


def create_list():
    employees = []
    identities = []
    c = 0
    print('start')
    with open(input_name, encoding='UTF-8') as fi:
        headers = fi.readline().split(delim)
        for idx, person in enumerate(fi.readlines()[:-1], 2):

            try:
                obj = Employee(zip(headers, person.split(delim)))
                if idx == 44: print(obj._arguments)
            except TimeoutError:
                # print('Я не знаю, что ты тут делаешь без должности', idx)
                c += 1
            except:
                print(idx)
                raise
            if obj.identity in identities:
                pass
                # employees[indexes[obj.identity]].Merge(obj)
            else:
                employees.append(obj)
                identities.append(obj.identity)
        # print(*zip(headers, fi.readlines()[19].split(delim)))

def export_list():
    with open(output_name, encoding='UTF-8') as fo:
        # dictionary записать заголовки - метод в csv
        for person in employees:
            person.Export()




data = load(open('person.js', encoding='UTF-8'))
for p in data['blank']:
    continue


create_list()
# with open(input_name, encoding='UTF-8') as fi:
#     print(fi.readlines())