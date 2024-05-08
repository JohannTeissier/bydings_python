#include <iostream>

#include "circle.hpp"

Point* get_position(Shape *shape)
{
    return shape->get_position();
}

int main()
{
    Circle c{15, Point{12, 12}};
    Point p = *get_position(&c);
    std::cout << p.get_x() << p.get_y() << std::endl;

    return 0;
}