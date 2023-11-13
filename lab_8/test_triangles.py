from lab_6.points import Point
from lab_8.triangles import Triangle
import pytest


def test_init_valid():
    t = Triangle(-1, 3, -3, -3, 2, 1)
    assert isinstance(t, Triangle)


def test_init_invalid():
    with pytest.raises(ValueError):
        Triangle(0, 0, 1, 1, 2, 2)


def test_triangle_from_points():
    points = [Point(0, 0), Point(1, 0), Point(0, 1)]
    triangle = Triangle.from_points(points)
    standard_triangle = Triangle(0, 0, 1, 0, 0, 1)
    assert triangle.pt1 == Point(0, 0)
    assert triangle.pt2 == Point(1, 0)
    assert triangle.pt3 == Point(0, 1)
    assert triangle == standard_triangle


def test_triangle_properties():
    triangle = Triangle(2, 2, 4, 0, 0, 0)
    assert triangle.top == 2
    assert triangle.left == 0
    assert triangle.bottom == 0
    assert triangle.right == 4
    assert triangle.width == 4
    assert triangle.height == 2
    assert triangle.topleft == Point(0, 2)
    assert triangle.bottomleft == Point(0, 0)
    assert triangle.topright == Point(4, 2)
    assert triangle.bottomright == Point(4, 0)


def test_str():
    t = Triangle(-1, 3, -3, -3, 2, 1)
    result = str(t)
    assert result == "[(-1, 3), (-3, -3), (2, 1)]"


def test_repr():
    t = Triangle(-1, 3, -3, -3, 2, 1)
    result = repr(t)
    assert result == "Triangle(-1, 3, -3, -3, 2, 1)"


def test_eq():
    t1 = Triangle(-1, 3, -3, -3, 2, 1)
    t2 = Triangle(-1, 3, -3, -3, 2, 1)
    assert t1 == t2


def test_ne():
    t1 = Triangle(-1, 3, -3, -3, 2, 1)
    t2 = Triangle(-10, 31, -3, -3, 2, 1)
    assert t1 != t2


def test_center():
    t = Triangle(0, 0, 2, 0, 1, 2)
    result = t.center()
    assert result == Point(1, 2 / 3)


def test_area():
    t = Triangle(-1, 3, -3, -3, 2, 1)
    result = t.area()
    assert result == 11


def test_move():
    t = Triangle(-1, 3, -3, -3, 2, 1)
    t.move(1, 1)
    assert t == Triangle(0, 4, -2, -2, 3, 2)


def test_make4():
    t = Triangle(2, 2, 4, 0, 0, 0)
    result = t.make4()
    assert result == (
        Triangle(2, 2, 3.0, 1.0, 1.0, 1.0),
        Triangle(1.0, 1.0, 2.0, 0.0, 0, 0),
        Triangle(1.0, 1.0, 3.0, 1.0, 2.0, 0.0),
        Triangle(3.0, 1.0, 4, 0, 2.0, 0.0))
