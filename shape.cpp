#include "shape.hpp"

Shape::Shape(Point position)
{
    this->_position = new Point{position};
    this->_shape_name = "Forme";
}

Shape::~Shape()
{
    delete this->_position;
}

Point *Shape::get_position() const
{
    return this->_position;
}

void Shape::set_position(Point point)
{
    this->_position->set_x(point.get_x());
    this->_position->set_y(point.get_y());
}

std::string Shape::get_name() const
{
    return this->_shape_name;
}
