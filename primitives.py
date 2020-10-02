from typing import Tuple
from dataclasses import dataclass

Rect = Tuple[Tuple[float, float], Tuple[float, float]]


def tuple_to_rect(r: Rect):
    """Transforms a Rect tuple to a Rectangle class."""
    c1 = Point(r[0][0], r[0][1])
    c2 = Point(r[1][0], r[1][1])
    return Rectangle(c1, c2)


@dataclass
class Point:
    x: int
    y: int


class Rectangle:
    def __init__(self, c1, c2):
        """Ensure that the lower left corner, c1, has a smaller x value"""
        self.c1: Point = c1
        self.c2: Point = c2
        if c2.x < c1.x:
            self.c1, self.c2 = self.c2, self.c1

    @property
    def x_segment(self):
        return sorted((self.c1.x, self.c2.x))

    @property
    def y_segment(self):
        return sorted((self.c1.y, self.c2.y))

    @property
    def length(self):
        return abs(self.c2.x - self.c1.x)

    @property
    def height(self):
        return abs(self.c2.y - self.c1.y)

    @property
    def area(self):
        return self.length * self.height

    def combine_coords(rect):
        x = tuple(sorted((rect[0][0], rect[1][0])))  # 0, 5 or 5, 0
        y = tuple(sorted((rect[0][1], rect[1][1])))
        print(f"r: {rect}, x: {x}, y:{y}")
        return x, y

    def __repr__(self):
        return f"c1: {self.c1} c2: {self.c2}"
