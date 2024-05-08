#pragma once

#include "shape.hpp"

class Circle : public Shape
{
    public:

        Circle(int radius, Point position);

        int get_radius() const;
        void set_radius(int radius);

    private:

        int _radius;
};