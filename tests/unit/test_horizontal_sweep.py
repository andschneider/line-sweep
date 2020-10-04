import pytest

from horizontal import horizontal_sweep
from main import build_rectangles
from events import build_events


active_segments = [
    # (rectangle, active rectangles, answer)
    ("r1", [0, 2], 3),
    ("r1", [0, 1, 2], 4),
    ("r1", [1, 2], 3),
    ("r3", [0, 1], 1),
    ("r4", [0, 1, 2], 0),
    ("r4", [1, 2], 0),
    ("r4", [1, 2, 3], 3),
    ("r5", [0, 1, 2], 2),
    ("r5", [1, 2, 3], 6),
    ("r8", [0, 1], 5),
    ("r8", [0, 1, 2], 6),
    ("r8", [1, 2, 3, 4], 8),
    ("r13", [0, 1, 2, 3], 3),
]


@pytest.mark.parametrize("rec, active, length", active_segments)
def test_horizontal_sweep(test_rectangles, rec, active, length):
    """Tests the horizontal sweep calculates the total overlapping length of rectangles.

    If looking at a drawing of the rectangles, the active ones represent the left most
    edge of the rectangle. These would set during the left to right sweep.
    """
    rects = build_rectangles(test_rectangles[rec]["rec"])
    events = build_events(rects, horizontal=True)

    # create the active set of rectangles that would be seen with the vertical sweep line
    a = set()
    for i in active:
        a.add(rects[i])

    # perform horizontal sweep from bottom to top
    total_swept = horizontal_sweep(events, a)
    print(total_swept)
    assert total_swept == length
