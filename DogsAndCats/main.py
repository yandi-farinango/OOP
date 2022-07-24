# OOP Tutorial
# https://www.youtube.com/watch?v=JeznW_7DlB0&t=7s
# Dog & Cat 28:52 timeStamp

"""
We will define a PET class
which has attributes name and age

Pet objects will have methods
show and speak
"""

"""
We will use our PET class to create
Cat and Dog objects 
"""
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}. I am a {type(self)} and I am {self.age} years old")

    def speak(self):
        print(f"My name is {self.name}. I am a {type(self)}. I dont know what TYPE of PET. I dont know what to say")

"""
Our Dog class inherits 
attributes and functions of PET

we no longer need our __init__ 
b/c we've inherited __init__ from our Super Class
"""
class Dog(Pet):
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    """
    Our speak method is pertaining to Dog objects
    and overrides Pet.speak
    Thus, objects of type Dog will respond with "BARK"
    """
    def speak(self):
        print(f"My name is {self.name}. I am a {type(self)} BARK")

"""
We define a Cat object of class PET
"""
class Cat(Pet):
    """
    Our CAT object has attributes specific for CAT
    So we will call super.()__init__(name,age)
    which passes the shared attributes to our PET class
    and
    we also add an additional parameter color
    pertaining only to Cat
    """
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"My name is {self.name}. I am a {type(self)} MEOW")

    def show(self):
        print(f"My name is {self.name}. I am a {self.color} {type(self)} MEOW")

"""
Fish does not have any unique methods or attributes 
and simply inherits all atributes declared in our Pet class
"""
class Fish(Pet):
    pass

p = Pet("Yandi", 27)
p.show()

c = Cat("Ariel", 20, "Brown")
c.show()

d = Dog("Bri", 18)
d.show()

e = Fish("Luna", 0)
e.show()

p.speak()
c.speak()
d.speak()
e.speak()


