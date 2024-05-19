#pragma once

#include "shape.hpp"

class Circle : public Shape
{
    public:

        Circle(Point position, int radius);
        Circle(Circle *circle);

        int get_radius() const;

    private:

        int _radius;
};