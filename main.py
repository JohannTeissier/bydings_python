import ctypes

lib = ctypes.CDLL("./lib.so")
handlePoint = ctypes.POINTER(ctypes.c_char)

lib.create_point.restype = handlePoint
lib.create_point.argtypes = [ctypes.c_int, ctypes.c_int]

lib.destroy_point.argtypes = [handlePoint]

lib.get_x.restype = ctypes.c_int
lib.get_x.argtypes = [handlePoint]

lib.get_y.restype = ctypes.c_int
lib.get_y.argtypes = [handlePoint]

lib.set_x.argtypes = [handlePoint, ctypes.c_int]

lib.set_y.argtypes = [handlePoint, ctypes.c_int]

class Point:

    def __init__(self, x, y, obj=None):
        if(obj == None):
            self.obj = lib.create_point(x, y)
            self.clone = False
        else:
            self.obj = obj
            self.clone = True

    def __del__(self):
        if not self.clone:
            lib.destroy_point(self.obj)

    def get_add(self):
        return self.obj

    def get_x(self):
        return lib.get_x(self.obj)
    
    def get_y(self):
        return lib.get_y(self.obj)
    
    def set_x(self, x):
        lib.set_x(self.obj, x)

    def set_y(self, y):
        lib.set_y(self.obj, y)

handleCircle = ctypes.POINTER(ctypes.c_char)
lib.create_circle.restype = handleCircle
lib.create_circle.argtypes = [ctypes.c_int, handlePoint]

lib.destroy_circle.argtypes = [handleCircle]

lib.get_radius.argtypes = [handleCircle]
lib.get_radius.restype = ctypes.c_int

lib.get_position.argtypes = [handleCircle]
lib.get_position.restype = handlePoint

class Circle:
    def __init__(self, radius, position):
        self.obj = lib.create_circle(radius, position.obj)
    
    def __del__(self):
        lib.destroy_circle(self.obj)

    def get_radius(self):
        return lib.get_radius(self.obj)
    
    def get_position(self):
        position_ptr = lib.get_position(self.obj)
        x = lib.get_x(position_ptr)
        y = lib.get_y(position_ptr)
        return Point(x, y, position_ptr)

point = Point(8, 12)
print(point.get_x())
print(point.get_y())
circle = Circle(45, point)
print(circle.get_radius())
point.set_x(5)
print(point.get_x())
print(circle.get_position().get_x())
print(circle.get_position().get_y())
circle.get_position().set_x(25)
print(circle.get_position().get_x())
print(circle.get_position().get_y())
