#include "circle.hpp"

extern "C"
{
    Point *create_point(int x, int y)
    {
        return new Point(x, y);
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

    Circle* create_circle(int radius, Point *center)
    {
        return new Circle(radius, *center);
    }

    void destroy_circle(Circle *circle)
    {
        delete circle;
    }

    int get_radius(Circle *circle)
    {
        return circle->get_radius();
    }

    Point* get_position(Circle *circle)
    {
        return circle->get_position();
    }
}