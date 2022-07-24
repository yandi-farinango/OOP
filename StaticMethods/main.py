# OOP Tutorial
# https://www.youtube.com/watch?v=JeznW_7DlB0&t=7s
# 51:56

class Math:
    def multiply(self, x):
        return x * 12

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10


# we do not need to create an instance of class Math
# add5 is a static method
# that does not not pertain to a particular instance
print(Math.add5(5))


# we create an instance m1 of class Math
m1 = Math()
# m1 can perform the method multiply
print(m1.multiply(2))

# m1 also has access to static method add5
print(m1.add5(5))


# this one prints an error b/c
# multiply is only available for instances of class Math
# Math is not an instance of class Math
print(Math.multiply(2))
