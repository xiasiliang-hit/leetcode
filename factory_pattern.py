from __future__ import generators
import random

class Factory(object):
    # Create based on class name:
    def getShape(type):
        #return eval(type + "()")
        if type == "Circle": return Circle()
        if type == "Square": return Square()
#        assert 0, "Bad shape creation: " + type
#    factory = staticmethod(factory)

class Shape(object): pass

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

# Generate shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes =  [ Factory.getShape(i) for i in shapeNameGen(7)]





for shape in shapes:
    shape.draw()
    shape.erase()


