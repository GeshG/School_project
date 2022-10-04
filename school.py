from symbol import return_stmt


class School:
    def __init__(self, rooms, students, teachers):
        self.rooms = rooms
        self.students = students
        self.teachers = teachers
        
    def student_calculation(self, student, score):
        self.student = student
        self.score = score
        student_accepted = 0
        
        for student in range(1, self.students+1):
            student_score = float(input())
            if 4.0 < student_score < 4.5:
                student_accepted +=1
            elif 5.0 < student_score < 5.5:
                student_accepted +=1
            else:
                student_accepted +=1
        
        if len(student_accepted) < 20:
            return (f'We have {len(student_accepted)} students. There is room for more {20 - len(student_accepted)}')
        else:
            return ('No more room for students')

    def teacher_calculation(self, teacher):
        self.teacher = teacher
        

class Teacher:
    def __init__(self, interest):
        self.interest = interest

class Student:
    def __init__(self, score):
        self.score = score

class Course:
    def __init__(self, teacher, interest):
        self.teacher = teacher
        self.interest = interest
    
    def assign_teachers(self):
        assign_teacher = 0
        if self.teacher.interest == 'History':
            assign_teacher +=1
        elif self.teacher.interest == 'Geography':
            assign_teacher +=1
        elif self.teacher.interest == 'Psycology':
            assign_teacher +=1
        return assign_teacher
    
            