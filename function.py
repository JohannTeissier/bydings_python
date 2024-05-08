import ctypes

lib = ctypes.CDLL("./lib.so")

handlePoint = ctypes.POINTER(ctypes.c_char)

lib.create_point.argtypes = [ctypes.c_int, ctypes.c_int]
lib.create_point.restype = handlePoint

lib.destroy_point.argtypes = [handlePoint]

lib.get_x.argtypes = [handlePoint]
lib.get_x.restype = ctypes.c_int

lib.get_y.argtypes = [handlePoint]
lib.get_y.restype = ctypes.c_int

lib.set_x.argtypes = [handlePoint, ctypes.c_int]

lib.set_y.argtypes = [handlePoint, ctypes.c_int]

handleShape = ctypes.POINTER(ctypes.c_char)

lib.create_shape.restype = handleShape
lib.create_shape.argtypes = [handlePoint]

lib.destroy_shape.argtypes = [handleShape]

lib.get_name.restype = ctypes.c_char_p
lib.get_name.argtypes = [handleShape]

lib.get_position.restype = handlePoint
lib.get_position.argtypes = [handleShape]

lib.set_position.argtypes = [handleShape, handlePoint]


lib.create_circle.restype = handleShape
lib.create_circle.argtypes = [ctypes.c_int, handleShape]

lib.destroy_circle.argtypes = [handleShape]

lib.get_radius.restype = ctypes.c_int
lib.get_radius.argtypes = [handleShape]

lib.set_radius.argtypes = [handleShape, ctypes.c_int]

#lib.func.argtypes = [ctypes.c_char_p]

#lib.func(ctypes.c_char_p("Hello".encode('utf-8')))

class Point:
    def __init__(self, x: int=None, y: int=None, obj: ctypes.c_void_p=None) -> None:
        if obj == None:
            self.__obj = lib.create_point(x, y)
            self.__copy = False
        else:
            self.__obj = obj
            self.__copy = True

    def __del__(self):
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
    def __init__(self, position: Point=None, obj: ctypes.c_void_p=None) -> None:
        if obj == None:
            self.__obj = lib.create_shape(position.obj)
            self.__copy = False
        else:
            self.__obj = obj
            self.__copy = True

    def __del__(self):
        if not self.__copy:
            lib.destroy_shape(self.__obj)

    @property
    def obj(self) -> ctypes.c_void_p:
        return self.__obj

    @property
    def name(self) -> str:
        return lib.get_name(self.__obj).decode('utf-8')
    
    @property
    def position(self) -> Point:
        return Point(obj=lib.get_position(self.__obj))
    
    @position.setter
    def position(self, position: Point) -> None:
        lib.set_position(self.__obj, position.obj)

class Circle(Shape):
    def __init__(self, radius: int = None, position: Point = None, obj: ctypes.c_void_p = None) -> None:
        if obj == None:
            #super().__init__(position)
            self.__obj = lib.create_circle(radius, position.obj)
            self.__copy = False
        else:
            #super().__init__(obj=obj)
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
    
    @radius.setter
    def radius(self, radius: int) -> None:
        lib.set_radius(self.__obj, radius)

        


def main():    
    circle = Circle(10, Point(12,24))
    c2 = Circle(obj=circle.obj)

    print(c2.position.x, c2.position.y)
    c2.position.x = 100
    c2.position.y = 200
    print(c2.position.x, c2.position.y)
    print(circle.position.x, circle.position.y)

if __name__ == '__main__':
    main()