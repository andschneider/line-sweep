import pytest

from horizontal import horizontal


segs = [
    ([[0, 5], [1.5, 4.5]], 3),
    ([[0, 5], [1.5, 4.5], [1, 8]], 4),
    ([[0, 5], [4, 8]], 1),
    ([[0, 5], [5, 8]], 0),
    ([[0, 5.5], [2, 4], [5, 6]], 2.5),
]


@pytest.mark.parametrize("segments, length", segs)
def test_horizontal_sweep(segments, length):
    height = horizontal(segments)
    print(height)
    assert height == length
