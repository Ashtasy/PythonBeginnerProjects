#class Animal:
#
#    alive=True
#   
#    def eat(self):
#        print("This animal is eating")
#    
#    def sleep(self):
#        print("This animal is sleeping")
#
#class Rabbit(Animal): #rabbit is the child class and Animal is parent class
#    def run(self):
#        print("This rabbit is running")
#class Fish(Animal):
#    def swim(self):
#        print("bros swimming")
#class Hawk(Animal):
#    def fly(self):
#        print("Its a flying hawk")
#
#rabbit=Rabbit()
#fish=Fish()
#hawk=Hawk()


# MULTI LEVEL INHERITANCE

#class Organism:
#    
#    alive = True

#class Animal(Organism):
#
#    def eat(self):
#        print("This animal is eating")
#
#class Dog(Animal):
#    
#    def bark(self):
#        print("This dog is barking")

#dog = Dog()



# MULTI LEVEL INHERITANCE
class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabbit()
hawk=Hawk()
fish=Fish()
