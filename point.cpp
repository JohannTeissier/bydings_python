#include "point.hpp"

Point::Point(int x, int y)
{
    this->_x = x;
    this->_y = y;
}

int Point::get_x()
{
    return this->_x;
}

int Point::get_y()
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

Point Point::operator*(Point obj)
{
    int x, y;

    x = this->_x * obj._x;
    y = this->_y * obj._y;

    Point temp{x, y};

    return temp;
}

Point Point::operator*(int value)
{
    int x, y;

    x = this->_x * value;
    y = this->_y * value;

    Point temp{x, y};

    return temp;
}

Point Point::operator+(Point obj)
{
    int x, y;

    x = this->_x + obj._x;
    y = this->_y + obj._y;

    Point temp{x, y};

    return temp;
}

Point Point::operator+(int value)
{
    int x, y;

    x = this->_x + value;
    y = this->_y + value;

    Point temp{x, y};

    return temp;
}
