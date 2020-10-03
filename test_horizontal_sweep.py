import pytest

from horizontal import horizontal


segs = [([[0, 5], [1.5, 4.5]], 3), ([[0, 5], [1.5, 4.5], [1, 8]], 4)]


@pytest.mark.parametrize("segments, length", segs)
def test_horizontal_sweep(segments, length):
    height = horizontal(segments)
    print(height)
    assert height == length
