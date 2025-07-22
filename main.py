from csv import DictReader
from json import load
from employee import *


ЕСЛИ ДОЛЖНОСТИ НЕТ - УДАЛЯТЬ!


input_name = '../Temp/fi.txt'
output_name = '../Temp/fo.csv'
delim = '\t'
# yo_check = False


def create_list():
    employees = []
    identities = []
    with open(input_name, encoding='UTF-8') as fi:
        headers = fi.readline().split(delim)
        cnt = 0
        for person in fi.readlines()[:-1]:
            obj = Employee(zip(headers, person.split(delim)))
            print(obj.identity)
            if obj.identity in identities:
                print('AAAAAA')
                # employees[indexes[obj.identity]].Merge(obj)
            else:
                employees.append(obj)
                identities.append(obj.identity)
    print(identities)


def export_list():
    with open(output_name, encoding='UTF-8') as fo:
        # dictionary записать заголовки - метод в csv
        for person in employees:
            person.Export()




data = load(open('person.js', encoding='UTF-8'))
for p in data['blank']:
    continue


create_list()