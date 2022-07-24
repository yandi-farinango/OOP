# Python OOP Concepts
# https://www.youtube.com/watch?v=JeznW_7DlB0&t=7s
# Students 20:10 vidTime

"""
We are defining a STUDENT class
with attributes name, age, grade

the STUDENT class has a function get_grade
which returns the grade
of the respective student OBJECT
"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # int between 0 - 100

    def get_grade(self):
        return self.grade

"""
We are defining a COURSE class
with attributes name, max_students

students [] is also an attribute of course 
"""
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    # we have an add_student function
    # that allows us to add a student to a course
    # if our course is not full     i.e len(students) < self.max_students
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    # we have a get_average_grade function
    # that return an average grade for the course
    def get_average_grade(self):
        value = 0
        # each student in students[] should have a grade
        # for student in students[]
        # we can access the grade using get_grade
        for student in self.students:
            # we can create a running sum of students grades using +=
            value += student.get_grade()
        # we divide running sum by number of students in students[]
        # to return our average
        return value / len(self.students)

s1 = Student("Yandi", 27, 100)
s2 = Student("Ariel", 28, 90)
s3 = Student("Jill", 20, 85)


course = Course("CS", 2)
course.add_student(s1)
course.add_student(s2)

"""
will NOT print names
b/c course.students is not a STUDENT object
and thus does not have STUDENT attributes

print(course.students.name)
"""

# course.students is an attribute of course
# course.students is an list object
# course.students is a LIST containing STUDENTS in the course
print(type(course.students))

print(course.get_average_grade())

print(course.add_student(s3))
