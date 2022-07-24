# OOP Tutorial
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:
    def __init__(self):
        pass

    def get_age(self):
        return self.age

    def get_name(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

e1 = Employee()
e1.set_name("Yandi")
e1.set_age(28)

print(f"Hi my name is {e1.name} and I am {e1.age} years old")
