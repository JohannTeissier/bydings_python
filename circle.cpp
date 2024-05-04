#include "circle.hpp"

Circle::Circle(int radius, Point position): Shape(position)
{
    this->_radius = radius;
    this->_shape_name = "Circle";
}

int Circle::get_radius() const
{
    return this->_radius;
}
