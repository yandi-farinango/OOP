class Person:
    """
    number_of_people is an attribute of the Person class
    aka class Attribute
    """
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # we update number_of_people
        # to maintain a running count
        Person.number_of_people = Person.number_of_people + 1

    def get_numberOfPeople(self):
        return self.number_of_people


# Create instances of person
P1 = Person("Yandi")
p2 = Person("Ariel")
"""
Person.number_of_people
returns 2
because the CLASS ATTRIBUTE number_of_people
was updated upon creating person p1

P1.get_numberOfPeople()
ALSO returns 2
because number_of_people is a CLASS ATTRIBUTE
and is applied to each Person
"""
print(Person.number_of_people)
print(P1.get_numberOfPeople())

p3 = Person("Bri")


print(Person.number_of_people)
print(P1.get_numberOfPeople())

