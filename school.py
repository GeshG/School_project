

class School:
    def __init__(self, name, chairs, rooms, capacity):
        self.capacity = capacity
        self.name = name
        self.chairs = chairs
        self.rooms = rooms
    
    #working
    def welcome_message(self):
        return (f'Welcome to {self.name}! We have a total of {self.chairs * self.rooms} vacancies for students in our school!')
    
    #not fully working 
    def accepted_students(self, student):
        course_class = []
        if 3.5 < student.stud_grade() <= 4.0:
            if len(student) < self.capacity:
                course_class.append(student)
        elif 4.1 <= student.stud_grade() <= 4.5:
            if len(student) < self.capacity:
                course_class.append(student)
        else:
            course_class.append(student)
        return (f'Assign students to course with grade {student.stud_grade()}. Students in course with capacity of {self.capacity}')
    

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def stud_grade(self):
        return self.grade


class Teacher:
    def __init__(self, name, skill, age):
        self.name = name
        self.skill = skill
        self.age = age

class Course:
    def __init__(self, course_name, course_capacity):
        self.course_name = course_name
        self.course_capacity = course_capacity
        

    #working
    def assign_teacher(self, teacher):
        if 1 < teacher.skill <= 80:
            if 20 < teacher.age <= 25:
                self.course_name
        elif 81 < teacher.skill <= 90:
            if 26 < teacher.age <= 30:
                self.course_name
        else:
            self.course_name
        return (f'Teacher {teacher.name} at the age of {teacher.age} will be assigned to {self.course_name}.')
    
    #not fully working -- check logic
    def assign_student(self, student):
        stud_course = []
        if 3.5 < student.stud_grade() < 4.0:
            if len(stud_course) < self.course_capacity:
                stud_course.append(student)
        elif 4.0 < student.stud_grade() < 4.5:
            if len(stud_course) < self.course_capacity:
                stud_course.append(student)
        elif 4.5 < student.stud_grade() < 5.0:
            if len(stud_course) < self.course_capacity:
                stud_course.append(student)
        return (f'Assign {self.course_name} course to students with {student.stud_grade()} grade. Currently accepted students {stud_course} out of {self.course_capacity}')
    

school1 = School('Hogwards', 20, 10, 3)
student1 = Student('Oukland', 3.5)
student2 = Student('Pete', 5.6)
course1 = Course('Philosophy', 2)
course2 = Course('Math', 3)
course3 = Course('Geography', 4)
teacher1 = Teacher('Tom', 80, 30)
teacher2 = Teacher('Sarah', 75, 22)
teacher3 = Teacher('Sven', 80, 40)
print(school1.welcome_message())
print(course1.assign_teacher(teacher1))
print(course2.assign_teacher(teacher2))
print(course3.assign_teacher(teacher3))
print(course1.assign_student(student1))
print(course1.assign_student(student2))
print(school1.accepted_students(student1))