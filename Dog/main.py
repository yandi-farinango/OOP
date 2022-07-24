# OOP Python Youtube Tutorial
# https://www.youtube.com/watch?v=JeznW_7DlB0&t=7s


class DOG():
    def __init__(self, name, age):
        # creates an object DOG
        # with an attribute name
        self.name = name
        self.age = age

    # Some functions that object Dog3 can do
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")


    # Getters and setters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age
        return age

    def setName(self, name):
        self.name = name
        return name


# Here we creating an object d
# of class DOG
# w name Yandi
d = DOG("Yandi", 27)

print(d.name, type(d)) # will print the name, dataType associated w object d

d.bark() # d can perform the functions within class dog

print(d.add_one(5)) # d performs the add_one function
                    # which takes a values
                    # and adds one

# Creates object d2
# of class DOG

# object d2 has the name attribute "Ariel"
d2 = DOG("Ariel", 24)
print(d2.name, type(d2))
d2.bark()
print(d2.add_one(2))

print("Names are: ", d.getName(), d2.getName())
print("Ages are: ", d.getAge(), d2.getAge())

# We can use our set function
# to override object d2's
# name and age attributes
d2.setName("OverRide")
d2.setAge(0)
print(d2.name, d2.age)
