#include "circle.hpp"

Circle::Circle(Point position, int radius) : Shape(position)
{
    this->_radius = radius;
    this->_name = "Circle";
}

Circle::Circle(Circle *circle) : Shape(*circle->_position)
{
    this->_radius = circle->_radius;
    this->_name = "Circle";
}

int Circle::get_radius() const
{
    return this->_radius;
}
