""" 
1.Writing down the objects on paper
2. Writing down the properties of the objects
3. Writing down the relationships between the objects
4. Writing a class for each object
5. Writing a method for each property
6. Calling the classes and their methods
"""

from random import randint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x  < rectangle.upright.y and \
            rectangle.lowleft.x < self.y < rectangle.upright.y:
            return True
        else:
            return False
        
    def distance(self, point):
        x_difference = self.x - point.x
        y_difference = self.y - point.y
        return ((x_difference)**2 + (y_difference)**2)**0.5
        
    

class Rectangle:
    
    def __init__(self, point1, point2):
        self.lowleft = point1
        self.upright = point2
    
    def area(self):
        return (abs(self.lowleft.x - self.upright.x) * abs(self.lowleft.y - self.upright.y))
        
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

print(rectangle.area())
print("Rectangle Coordinates: ", 
      rectangle.lowleft.x, ", ",
      rectangle.lowleft.y, "and", 
      rectangle.upright.x, ",",
      rectangle.upright.y)

user_point = Point(float(input("Gues x: ")),
                   float(input("Guess y: ")))

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangele: ", 
      user_point.falls_in_rectangle(rectangle))

print("Your area was off by: ", 
      rectangle.area() - user_area)




# print(point1.x)
# print(point1.y)
# print(point1.distance(point2))
# class Point2:
#     def __init__(this_object, x, y):
#         print(f"x = {x}")
#         print(f"y = {y}")
#         this_object.x = 5
#         this_object.y = y

# print(point1.falls_in_rectangle((7, 15), (15, 25)))

























