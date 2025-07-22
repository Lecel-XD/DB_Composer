from csv import DictReader
from json import load

input_name = '../Temp/fi.csv'
output_name = '../Temp/fo.csv'
# yo_check = False

data = load(open('person.js'))
for p in data['blank']:
    print(p)
print(data)

class Employee:
    def __init__(self, **kwargs):
        self._constant = {}
        self.identity = 1
        for x, y in kwargs.items():
            self._constant = self._constant.get(x, 0) + int(y)
    def __eq__(self, other):
        return self.identity == other.identity
    # в ините сделать разбиение выплат на категории (постоянные, субсидии и т.д.)
    def Export(self):
        pass
    def Merge(self, obj):
        pass


def main():
    # основные переменные
    employees = []
    indexes = {}
    counter = 0
    before_counting_rows = ['', 'Месяц начисления', 'Организация', 'Сотрудник.Таб. номер', 'Должность', 'Подразделение', 'Сотрудник.Физическое лицо.Пол', 'Сотрудник', 'Сальдо на начало месяца']
    # экспорт должен брать первый столбец из identity, а не вычислять его заново



    # создание списка сотрудников без дубликатов
    with open(input_name) as fi:
        dictionary = DictReader(fi, delimiter=',')
        for person in dictionary:
            obj = Employee(**person)
            if obj.identity in indexes:
                employees[indexes[obj.identity]].Merge(obj)
            else:
                employees.append(obj)
                indexes[obj.identity] = counter
                counter += 1


    # экспорт данных
    with open(output_name, encoding='UTF-8') as fo:
        # dictionary записать заголовки - метод в csv
        for person in employees:
            person.Export()