from csv import DictReader


input_name = '../Temp/fi.csv'
output_name = '../Temp/fo.csv'
yo_check = False


class Employee:
    identity = 1
    # в ините сделать разбиение выплат на категории (постоянные, субсидии и т.д.)
    def Export(self):
        pass
    def PrintHeader(self):
        pass
    def Merge(self, obj):
        pass


# основные переменные
employees = []
indexes = {}
counter = 0
before_counting_rows = ['', 'Месяц начисления', 'Организация']
# экспорт должен брать первый столбец из identity, а не вычислять его заново



# создание списка сотрудников без дубликатов
with open(input_name) as fi:
    for person in DictReader(fi, delimiter=','):
        obj = Employee(person)
        if obj.identity in indexes:
            employees[indexes[obj.identity]].Merge(obj)
        else:
            employees.append(obj)
            indexes[obj.identity] = counter
            counter += 1


# экспорт данных
with open(output_name, encoding='UTF-8') as fo:
    Employee.PrintHeader()
    for person in employees:
        person.Export()