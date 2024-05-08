#include <iostream>
#include <string>

#include "point.hpp"
#include "shape.hpp"
#include "circle.hpp"

extern "C"
{
    Point* create_point(int x, int y)
    {
        return new Point{x, y};
    }

    void destroy_point(Point* point)
    {
        delete point;
    }

    int get_x(Point *point)
    {
        return point->get_x();
    }

    int get_y(Point *point)
    {
        return point->get_y();
    }

    void set_x(Point *point, int x)
    {
        point->set_x(x);
    }

    void set_y(Point *point, int y)
    {
        point->set_y(y);
    }

    void func(char* phrase)
    {
        std::string s{phrase};
        std::cout << s << std::endl;
    }

    Shape* create_shape(Point *position)
    {
        return new Shape{*position};
    }

    void destroy_shape(Shape *shape)
    {
        delete shape;
    }

    const char* get_name(Shape *shape)
    {
        return shape->get_name().c_str();
    }

    Point* get_position(Shape *shape)
    {
        return shape->get_position();
    }

    void set_position(Shape *shape, Point *position)
    {
        shape->set_position(*position);
    }

    Circle* create_circle(int radius, Point* point)
    {
        return new Circle{radius, *point};
    }

    void destroy_circle(Circle *circle)
    {
        delete circle;
    }

    int get_radius(Circle *circle)
    {
        return circle->get_radius();
    }

    void set_radius(Circle *circle, int radius)
    {
        circle->set_radius(radius);
    }
}