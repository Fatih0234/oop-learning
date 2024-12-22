


class Parent:
    hair_color = "brown"

class Child(Parent):
    pass


# You can change the attributes you inherit from the parent class.

class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"
    
# Extending the parent class
# You can also extend the parent class by defining additional attributes and methods in the child class.

class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")
        
        
        
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))


print(jim.speak("Woof"))


print(jack.speak("Woof"))


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks; {sound}"
    
# ...

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

print(isinstance(miles, Dog)) # True
print(isinstance(miles, Bulldog)) # False
print(isinstance(jack, Dog)) # True
print(isinstance(jack, Bulldog)) # True
print(type(miles))


# Parent Class Functionality Extension
# ...

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

# but sometiems dogs make different sounds
print(miles.speak("Grrr"))

jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
    
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

a = Dog("a", 1)
print(a.speak("bark"))