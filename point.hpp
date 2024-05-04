class Point
{
    public:

        Point(int x, int y);

        int get_x();
        int get_y();
        void set_x(int x);
        void set_y(int y);

        Point operator*(Point obj);
        Point operator*(int value);
        Point operator+(Point obj);
        Point operator+(int value);

    private:

        int _x;
        int _y;
};