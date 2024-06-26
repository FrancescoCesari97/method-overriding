
# * method overriding

# class Animal:

#     def eat(self):
#         print("this animal is eating")

# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating a carrot")

# rabbit = Rabbit()
# rabbit.eat()



# * method chaining

    # * method chaining = calling multiple methods sequentialy
    # *                   each call performs an action on the same object amd returns self  

class Car:

    def turn_on(slef):
        print("You start the engine")
        return slef

    def drive(slef):
        print("You drive the car")
        return slef

    def brake(slef):
        print("You step on the brakes")
        return slef
    
    def turn_off(slef):
        print("You turn off the engine")
        return slef
    
car = Car()

# car.turn_on().drive()
car.brake().turn_off()
