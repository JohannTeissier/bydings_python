#pragma once

#include "shape.hpp"

class Circle: public Shape
{
    public:

        Circle(int radius, Point position);

        int get_radius() const;

    private:

        int _radius;
};