from function import Point
from function import Shape
from function import Circle

def main():
    circle = Circle(10, Point(12,24))
    c2 = Circle(obj=circle.obj)
    shape = Shape(Point(12, 35))

    print(c2.position.x, c2.position.y)
    c2.position.x = 100
    c2.position.y = 200
    print(c2.position.x, c2.position.y)
    print(circle.position.x, circle.position.y)
    print(circle.name)

    print(shape.name)
    print(shape.position.x, shape.position.y)

if __name__ == '__main__':
    main()