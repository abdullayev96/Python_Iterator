####################  Polymorphism  in OOP prinsp

class Car:
  def start(self):
    return "🚗 Mashina yurdi"


class Computer:
  def start(self):
    return "💻 Kompyuter yondi"


class Fridge:
  def start(self):
    return "🧊 Muzlatkich sovitishni boshladi"


# Polymorphism: start() har xil ishlayapti
devices = [Car(), Computer(), Fridge()]

for device in devices:
  print(device.start())



###########   2
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Drive!")
#
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Sail!")
#
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object
#
# for x in (car1, boat1, plane1):
#   x.move()