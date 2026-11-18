class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = [] #assoc

    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name

    def add_student(self, student):
        self.students.append(student)

class School:
    def __init__(self, name):
        self.name = name
        self.students = [] #list of students

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"Students in {self.name}:")
        for student in self.students:
            print(student.name)


school = School("Riverside High")
s1 = Student("Ara")
s2 = Student("Bobby")

school.add_student(s1)
school.add_student(s2)

school.display_students()
print()
s3 = Student("Enrique")
school.add_student(s3)
school.display_students()
print()
for student in school.students:
    print(f"Student Name: {student.name}")