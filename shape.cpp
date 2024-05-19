#include "shape.hpp"

Shape::Shape(Point position)
{
    this->_name = "Forme";
    this->_position = new Point{position};
}

Shape::Shape(Shape *shape)
{
    this->_name = "Forme";
    this->_position = new Point{*shape->_position};
}

Shape::~Shape()
{
    delete this->_position;
}

const Point& Shape::get_position() const
{
    return *(this->_position);
}

void Shape::set_position(Point position)
{
    this->_position->set_x(position.get_x());
    this->_position->set_y(position.get_y());
}

std::string Shape::get_name() const
{
    return this->_name;
}
