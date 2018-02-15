from __future__ import generators
import random
import abc


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
#def shapeNameGen(n):
#    types = Shape.__subclasses__()
#    for i in range(n):
#        yield random.choice(types).__name__

#shapes =  [ Factory.getShape(i) for i in shapeNameGen(7)]


#for shape in shapes:
#    shape.draw()
#    shape.erase()



class Shape2:
    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError

class Rectangle(Shape2):
    def draw(self):
        print "rect"


class Circle(Shape2):
    def draw(self):
        print "circle"
        


class ShapeFactory:
    @classmethod
    def getShapeById(self,id):
        if id == "rect":
            return Rectangle()
        elif id == "circle":
            return Circle()


if __name__ == "__main__":
    shape_ins = ShapeFactory.getShapeById("rect")
    shape_ins.draw()

    print round(1.2)
    print round(1.6)





