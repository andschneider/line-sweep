from typing import Tuple
from dataclasses import dataclass

Rect = Tuple[Tuple[float, float], Tuple[float, float]]


def tuple_to_rect(r: Rect):
    """Transforms a Rect tuple to a Rectangle class.

    Ensures the ordering of the points in the rectangle is such that
    the lower left point, c1, has both smaller x and y values. Thus,
    the upper right point, c2, has larger x and y values.
    """
    c1 = Point(min(r[0][0], r[1][0]), min(r[0][1], r[1][1]))
    c2 = Point(max(r[0][0], r[1][0]), max(r[0][1], r[1][1]))
    return Rectangle(c1, c2)


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Rectangle:
    c1: Point
    c2: Point

    @property
    def x_segment(self):
        return self.c1.x, self.c2.x

    @property
    def y_segment(self):
        return self.c1.y, self.c2.y

    @property
    def length(self):
        return abs(self.c2.x - self.c1.x)

    @property
    def height(self):
        return abs(self.c2.y - self.c1.y)

    @property
    def area(self):
        return self.length * self.height

    def __repr__(self):
        return f"c1: {self.c1} c2: {self.c2}"
