###########  OOP

########   Boshlangich
# class MyClass:
#   x = 5
#
# a=MyClass()
# print(a.x)



###############   __init__ method dan foydalanish


# class Person:
#   def __init__(self, name, age, address):
#     self.name = name
#     self.age = age
#     self.age1 = address
#
# p1 = Person("John", 36, "Al-baxt")
#
# print(p1.name)
# print(p1.age)
# print(p1.age1)


#####     str method


class Person:

  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address


  def __str__(self):
    return f"{self.name}||{self.age}||{self.address}"

p1 = Person("John", 36, "Farobiy")

print(p1)