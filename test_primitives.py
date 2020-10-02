import pytest

from primitives import Point, tuple_to_rect

rects = [
    (((0, 0), (5, 5)), 25),
    (((7, 1), (1, 8)), 42),
    (((-1, 4.5), (5.5, 1.5)), 19.5),
]


@pytest.mark.parametrize("rect, area", rects)
def test_rectange_class(rect, area):
    r = tuple_to_rect(rect)
    assert r.area == area

def test_x_segment():
    r = tuple_to_rect(rects[1][0])
    print(r.x_segment())
    print(r.y_segment())

def test_create_point():
    rect = rects[0][0]
    c1 = Point(rect[0][0], rect[0][1])
    c2 = Point(rect[1][0], rect[1][1])
    assert c1 == Point(0, 0)
    assert c2 == Point(5, 5)
