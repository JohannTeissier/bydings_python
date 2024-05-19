#include "point.hpp"

Point::Point(int x, int y) : _x(x), _y(y)
{
}

int Point::get_x() const
{
    return this->_x;
}

int Point::get_y() const
{
    return this->_y;
}

void Point::set_x(int x)
{
    this->_x = x;
}

void Point::set_y(int y)
{
    this->_y = y;
}
