import ctypes

lib = ctypes.CDLL("./lib.so")

#------------Point------------#

handlePoint = ctypes.POINTER(ctypes.c_void_p)

lib.create_point.argtypes = [ctypes.c_int, ctypes.c_int]
lib.create_point.restype = handlePoint

lib.copy_point.argtypes = [handlePoint]
lib.copy_point.restype = handlePoint

lib.destroy_point.argtypes = [handlePoint]

lib.get_x.argtypes = [handlePoint]
lib.get_x.restype = ctypes.c_int

lib.get_y.argtypes = [handlePoint]
lib.get_y.restype = ctypes.c_int

lib.set_x.argtypes = [handlePoint, ctypes.c_int]

lib.set_y.argtypes = [handlePoint, ctypes.c_int]

#------------Shape------------#

handleShape = ctypes.POINTER(ctypes.c_void_p)

lib.create_shape.argtypes = [handlePoint]
lib.create_shape.restype = handleShape

lib.copy_shape.argtypes = [handleShape]
lib.copy_shape.restype = handleShape

lib.destroy_shape.argtypes = [handleShape]

lib.get_name.argtypes = [handleShape]
lib.get_name.restype = ctypes.c_char_p

lib.get_position.argtypes = [handleShape]
lib.get_position.restype = handlePoint

lib.set_position.argtypes = [handleShape, handlePoint]

#------------Circle------------#

lib.create_circle.argtypes = [handlePoint, ctypes.c_int]
lib.create_circle.restype = handleShape

lib.copy_circle.argtypes = [handleShape]
lib.copy_circle.restype = handleShape

lib.destroy_circle.argtypes = [handleShape]

lib.get_radius.argtypes = [handleShape]
lib.get_radius.restype = ctypes.c_int

class Point:
    def __init__(self, x: int=None, y: int=None, point: 'Point'=None, obj: ctypes.c_void_p|'Point'=None) -> None:
        if obj == None:
            if point == None:
                self.__obj = lib.create_point(x, y)
            else:
                if type(point) == Point:
                    point = point.obj
                self.__obj = lib.copy_point(point)
            self.__copy = False
        else:
            if type(obj) == Point:
                obj = obj.obj
            self.__obj = obj
            self.__copy = True

    def __del__(self) -> None:
        if not self.__copy:
            lib.destroy_point(self.__obj)

    @property
    def obj(self) -> ctypes.c_void_p:
        return self.__obj
    
    @property
    def x(self) -> int:
        return lib.get_x(self.__obj)
    
    @property
    def y(self) -> int:
        return lib.get_y(self.__obj)
    
    @x.setter
    def x(self, x: int) -> None:
        lib.set_x(self.__obj, x)

    @y.setter
    def y(self, y: int) -> None:
        lib.set_y(self.__obj, y)
    

class Shape:
    def __init__(self, position: Point=None, shape: 'Shape'=None, obj: ctypes.c_void_p|'Shape'=None) -> None:
        if obj == None:
            if shape == None:
                if type(position) == Point:
                    position = position.obj
                self.__obj = lib.create_shape(position)
            else:
                if type(shape) == Shape:
                    shape = shape.obj
                self.__obj = lib.copy_shape(shape)
            self.__copy = False
        else:
            if type(obj) == Shape:
                obj = obj.obj
            self.__obj = obj
            self.__copy = True

    def __del__(self) -> None:
        if not self.__copy:
            lib.destroy_shape(self.__obj)

    @property
    def obj(self):
        return self.__obj
    
    @property
    def name(self) -> str:
        return lib.get_name(self.__obj).decode('utf-8')
    
    @property
    def position(self) -> Point:
        return Point(point=lib.get_position(self.__obj))
    
    @position.setter
    def position(self, position: Point) -> None:
        if type(position) == Point:
            position = position.obj
        lib.set_position(self.__obj, position)
    
class Circle(Shape):
    def __init__(self, position: Point=None, radius: int=None, circle: 'Circle'=None, obj: ctypes.c_void_p|'Circle'=None) -> None:
        if obj == None:
            if circle == None:
                if type(position) == Point:
                    position = position.obj
                self.__obj = lib.create_circle(position, radius)
            else:
                if type(circle) == Circle:
                    circle = circle.obj
                self.__obj = lib.copy_circle(circle)
            self.__copy = False
        else:
            if type(obj) == Circle:
                obj = obj.obj
            self.__obj = obj
            self.__copy = True
        super().__init__(obj=self.__obj)

    def __del__(self) -> None:
        if not self.__copy:
            lib.destroy_circle(self.__obj)

    @property
    def obj(self) -> ctypes.c_void_p:
        return self.__obj
    
    @property
    def radius(self) -> int:
        return lib.get_radius(self.__obj)
    
def main():
    p = Point(15, 24)
    c1 = Circle(p, 15)
    c = Circle(circle=c1)
    print(c.name)
    print(c.position.x, c.position.y)
    c.position = Point(33, 44)
    print(c.position.x, c.position.y)
    print(c.radius)

if __name__ == '__main__':
    main()
