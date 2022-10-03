
class StudentScholarship:
    def student_scholarship(self, students):
        print('Calculating Scholarship')
        print('=======================')
        for student in students:
            print(f'{student.name} has score of {student.score}.')
            print(f'They will receive a mothly scholarship of {student.calculate_scholarship()}.')
    

class StudentFeeSemester:
    def student_fee_semester(self, students):
        for student in students:
            print('Calculating Semester Fee')
            print('========================')
            print(f'{student.name} from {student.country} will be paying {student.calculate_fee()}')


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Monthly_Scholarship(Student):
    def __init__(self, name, score, scholarship):
        super().__init__(name, score)
        self.scholarship = scholarship
        
    def calculate_scholarship(self):

        if self.score <= 4.5:
            return self.scholarship * 0.8
        else:
            return self.scholarship
        

class Student_Fee(Student):
    def __init__(self, name, score, country):
        super().__init__(name, score)
        self.country = country


    def calculate_fee(self):
        if  self.country == 'US' or self.country == 'Canada' or self.country == 'Dubai':
            #if 4.0 < self.score < 4.5:
                self.fee = 200
        elif self.country == 'France' or self.country == 'Spain' or self.country == 'Greece':
            #if 4.5 < self.score < 5.0:
                self.fee = 150
        else:
            self.fee = 220
        return self.fee