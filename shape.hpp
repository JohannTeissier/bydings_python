#pragma once

#include <string>

#include "point.hpp"

class Shape
{
    public:

        Shape(Point position);
        Shape(Shape *shape);
        ~Shape();

        const Point& get_position() const;
        void set_position(Point position);
        std::string get_name() const;

    protected:

        std::string _name;
        Point *_position;
};