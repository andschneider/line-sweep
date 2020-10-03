import pytest

from primitives import Point, tuple_to_rect

rects = [
    # (rectangle, area)
    (((0, 0), (5, 5)), 25),
    (((7, 1), (1, 8)), 42),
    (((-1, 4.5), (5.5, 1.5)), 19.5),
]


@pytest.mark.parametrize("rect, area", rects)
def test_rectangle_class(rect, area):
    r = tuple_to_rect(rect)
    assert r.area == area


def test_segments():
    r = tuple_to_rect(rects[1][0])
    assert r.x_segment == (1, 7)
    assert r.y_segment == (1, 8)


def test_create_point():
    rect = rects[0][0]
    c1 = Point(rect[0][0], rect[0][1])
    c2 = Point(rect[1][0], rect[1][1])
    assert c1 == Point(0, 0)
    assert c2 == Point(5, 5)


def test_create_point_reorder():
    """Test that the points are reordered correctly, with c1 being lower left and c2 being upper right."""
    r = tuple_to_rect(rects[2][0])
    assert r.c1 == Point(-1, 1.5)
    assert r.c2 == Point(5.5, 4.5)
