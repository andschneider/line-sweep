import heapq

import pytest

from horizontal import horizontal_sweep


segs = [
    # (segments, answer)
    ([[0, 5], [1.5, 4.5]], 3),
    ([[1.5, 4.5], [0, 5]], 3),
    ([[0, 5], [1.5, 4.5], [1, 8]], 4),
    ([[0, 5], [4, 8]], 1),
    ([[0, 5], [5, 8]], 0),
    ([[0, 5.5], [2, 4], [5, 6]], 2.5),
    ([[0, 7], [2, 4], [5, 6], [5.5, 8]], 4),
]


@pytest.mark.parametrize("segments, length", segs)
def test_horizontal_sweep(segments, length):
    heapq.heapify(segments)
    height = horizontal_sweep(segments)
    print(height)
    assert height == length
