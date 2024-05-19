from function import Point
from function import Shape
from function import Circle

p1 = Point(12, 15)
c1 = Circle(p1, 123)
print(c1.position.x, c1.position.y)
print(c1.name)
p1.x = 100
p1.y = 200
print(c1.position.x, c1.position.y)
c1.position.x = 456
c1.position.y = 0
print(c1.position.x, c1.position.y)
c1.position = Point(99, 88)
print(c1.position.x, c1.position.y)


#print(s.position.x, s.position.y)
