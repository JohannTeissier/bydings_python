#pragma once

#include <string>

#include "point.hpp"

class Shape
{
    public:

        Shape(Point position);
        ~Shape();

        Point* get_position() const;

    protected:

        std::string _shape_name;
        Point *_position;
};