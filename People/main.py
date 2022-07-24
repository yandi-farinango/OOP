# OOP Tutorial
# https://www.youtube.com/watch?v=JeznW_7DlB0&t=7s
# 40:50 Time Stamp

class Person:
    """
    number_of_people is an attribute of the class Person
    aka CLASS ATTRIBUTE
    meaning it is defined for the ENTIRE class
    and not specific to any particular INSTANCE of a class
    """
    people = 0

    def __init__(self, name):
        self.name = name
        # for every instance of Person created
        # we call classMethod add_person()
        Person.add_person()

    # each instance of Person created
    # has a people attribute associated
    def get_numberOfPeople(self):
        return self.people

    # our class Methods can be used
    # within our class
    # this is how we added a person earlier
    @classmethod
    def number_of_people_(cls):
        return cls.people

    @classmethod
    def add_person(cls):
        cls.people += 1


P1 = Person("Yandi")
p2 = Person("Ariel")

# Person class has an attribute people
print(Person.people)
# Person class also has a method number_of_people()
print(Person.number_of_people_())
# An instance of person has a method which returns the number_of_People
print(P1.get_numberOfPeople())
