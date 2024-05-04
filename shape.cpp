#include "shape.hpp"

Shape::Shape(Point position)
{
    this->_shape_name = "Form";
    this->_position = new Point{position};
}

Shape::~Shape()
{
    delete this->_position;
}

Point* Shape::get_position() const
{
    return this->_position;
}
