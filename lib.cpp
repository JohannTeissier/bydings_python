#include "point.hpp"
#include "shape.hpp"
#include "circle.hpp"

extern "C"
{
    /*------------Point------------*/

    Point* create_point(int x, int y)
    {
        return new Point{x, y};
    }

    Point* copy_point(Point *point)
    {
        return new Point{*point};
    }

    void destroy_point(Point *point)
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

    /*------------Shape------------*/

    Shape* create_shape(Point *position)
    {
        return new Shape{*position};
    }

    Shape* copy_shape(Shape *shape)
    {
        return new Shape{shape};
    }

    void destroy_shape(Shape *shape)
    {
        delete shape;
    }

    const char* get_name(Shape *shape)
    {
        return shape->get_name().c_str();
    }

    const Point* get_position(Shape *shape)
    {
        return &(shape->get_position());
    }

    void set_position(Shape *shape, Point *position)
    {
        shape->set_position(*position);
    }

    /*------------Circle------------*/

    Circle* create_circle(Point *position, int radius)
    {
        return new Circle{*position, radius};
    }

    Circle* copy_circle(Circle *circle)
    {
        return new Circle{circle};
    }

    void destroy_circle(Circle *circle)
    {
        delete circle;
    }

    int get_radius(Circle *circle)
    {
        return circle->get_radius();
    }
}