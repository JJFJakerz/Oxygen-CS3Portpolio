class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.student = []

    def add_student(self, student):
        self.student.append(student)

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)


math = Course("Mathematics")
science = Course("Science")

student1 = Student("José Protasio Rizal Mercado y Alonso Realonda", "9")
student2 = Student("Maria Santos", "7")
student3 = Student("Juan Dela Cruz", "8")

teacher1 = Teacher("Ms. Cruz", "Mathematics")

teacher1.grade = student1.grade  
teacher1.student = student1
teacher1.student.grade = student1.grade  

print(teacher1.name)
print(teacher1.subject)       
print()
print(teacher1.student.name)
print(teacher1.student.grade)
print()

teacher1 = Teacher("Ms. Cruz", "Mathematics")
teacher1.add_student(student1)
teacher1.add_student(student2)
teacher1.add_student(student3)

for student in teacher1.student:
    print(student.name)

student1.enroll(math)
student1.enroll(science)
student2.enroll(math)

teacher1 = Teacher("Ms. Cruz")
teacher1.introduce()
