from datetime import date

class Employee:
    def __init__(self, fullname, birth_date, salary):
        self._fullname = fullname
        self._birth_date = birth_date
        self._salary = salary

    @property
    def fullname(self):
        return self._fullname

    @property
    def salary(self):
        return self._salary
    
    def surname(self):
        return self._fullname.strip().split(' ')[-1]

    def age(self):
        birth_date_splitted = self._birth_date.split('/')
        birth_year =  birth_date_splitted[-1]
        actual_year = date.today().year
        return actual_year - int(birth_year)

    def calculate_salary_bonus(self):
        value = self._salary * 0.1
        if value > 1000:
            raise Exception('O SALÁRIO É MUITO ALTO PARA RECEBER BÔNUS.')
        return value
    
    def is_associate(self):
        surnames = ['Musk', 'Gates']
        return (self.surname() in surnames) and (self._salary >= 100000)
    
    def decrease_salary(self):
        if self.is_associate():
            decrease = self._salary * 0.1
            self._salary = self._salary - decrease

    def __str__(self):
        return f'Employee({self._fullname}, {self._birth_date}, {self._salary})'