#pragma once

#include <string>

#include "point.hpp"

class Shape
{
    public:

        Shape(Point position);
        ~Shape();

        Point* get_position() const;
        void set_position(Point point);
        std::string get_name() const;

    protected:

        std::string _shape_name;
        Point *_position;
};