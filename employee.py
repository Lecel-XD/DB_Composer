class Employee:
    def __init__(self, lst):
        dictionary = {}
        for x, y in lst:
            x, y = x.strip(), y.strip()
            if not y:
                dictionary[x] = dictionary.get(x, 0)
            elif y[0].isalpha():
                dictionary[x] = y
            else:
                dictionary[x] = dictionary.get(x, 0) + float(y.replace(',', '.'))
        self._arguments = dictionary
        self.identity = dictionary['Месяц начисления'] + dictionary['Организация'] + dictionary['Должность'] + dictionary['Подразделение'] + dictionary['Сотрудник']


    def __eq__(self, other):
        return self.identity == other.identity
    # в ините сделать разбиение выплат на категории (постоянные, субсидии и т.д.)
    def Export(self):
        pass
    def Merge(self, obj):
        pass
