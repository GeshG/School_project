
class PayRoll:
    def calculate_payroll(self, teachers):
        print('Calculating Salary')
        print('==================')
        for teacher in teachers:
            print(f'Payment for {teacher.id} - {teacher.first_name} {teacher.last_name}')
            print(f'Gross monthly salary - {teacher.gross_monthly_salary()}, where tax is 20%')
            print(f'Taxes - {teacher.monthly_salary_taxFee()}')
            print(f'Net salary without bonus - {teacher.gross_monthly_salary() - teacher.monthly_salary_taxFee()}')
            print(f'Bonus based on skill and age -  {teacher.bonus()}')
            print('')
        
    
    
class Teacher:

    def __init__(self, id, first_name, last_name, age, skill):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skill = skill


class MonthlySalaryTeacher(Teacher): 

    def __init__(self, id, first_name, last_name, age, skill, monthly_salary):
        super().__init__(id, first_name, last_name, age, skill)
        self.monthly_salary = monthly_salary
        
    
    def gross_monthly_salary(self):
        return self.monthly_salary
    
    def monthly_salary_taxFee(self):
        return self.monthly_salary * 0.2

    def bonus(self):
        self.bonuses = 0
        if 70 < self.skill < 80 and 20 < self.age < 25:
            self.bonuses = self.monthly_salary * 0.15
        elif 80 < self.skill < 90 and 25 < self.age < 30:
            self.bonuses = self.monthly_salary * 0.20
        elif self.skill >= 95 and 30 < self.age < 35:
            self.bonuses = self.monthly_salary * 0.25
        else:
            self.bonuses= self.monthly_salary * 0.30
        return self.bonuses

class HonoredTeacher(Teacher):

    def __init__(self, id, first_name, last_name, age, skill, hours_worked, hours_rate):
        super().__init__(id, first_name, last_name, age, skill)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def gross_monthly_salary(self):
        return self.hours_worked * self.hours_rate

    def monthly_salary_taxFee(self):
        after_tax = (self.hours_worked * self.hours_rate * 0.2)
        return after_tax
    
    def bonus(self):
        self.bonuses = 0
        if 70 < self.skill < 80 and 27 < self.age < 32:
            self.bonuses = self.hours_worked* self.hours_rate * 0.12
        elif 80 < self.skill < 90 and 29 < self.age < 34:
            self.bonuses = self.hours_worked* self.hours_rate * 0.14
        elif self.skill >= 95 and 30 < self.age < 35:
            self.bonuses = self.hours_worked* self.hours_rate * 0.16
        else:
            self.bonuses = self.hours_worked* self.hours_rate * 0.18
        return round(self.bonuses, 0)
    
    #def total_income(self):
       #return self.bonuses + self.after_tax
        