

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
jefry = Dog("Jefry", 5)
print(jefry.name)
print(jefry.age)

# name and age are instance attributes that
# belongs to specific instances of the Dog class.

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# On the other hand, species is a class attribute.
# It is global in scope and belongs to the Dog class itself.

print(Dog("Jefry", 5)) # <__main__.Dog object at 0x000002733DF1C150>

a = Dog("Jefry", 5)
b = Dog("Jefry", 5)
print(a == b) # False, two distinct objects in memory



# custom objects are mutable by default
# This means that you can change their attributes
# after you create them.

a.age = 6
print(a.age) # 6

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    

miles = Dog("Miles", 4)
print(miles.description()) # Miles is 4 years old
print(miles.speak("Woof Woof")) # Miles says Woof Woof
print(miles.speak("Bow Wow")) # Miles says Bow Wow

names = ["Fido", "Buddy", "Rex", "Miles", "Milo", "Max"]

print(names) # ['Fido', 'Buddy', 'Rex', 'Miles', 'Milo', 'Max']

print(miles) # <__main__.Dog object at 0x000002733DF1C150>

# The __str__ method is a special method that returns a string representation of an object.
# You can call it by using the str() constructor.
# This is useful for debugging and logging.
print(str(miles)) # Miles is 4 years old
print(miles)

# Methods like .__init__() and .__str__() are called dunder methods 
# because they begin and end with double underscores.

