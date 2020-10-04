import heapq
import json

import pytest

from horizontal import horizontal_sweep, horizontal_sweep2
from main import build_rectangles, build_events

segs = [
    # (segments, answer)
    # ([[0, 5], [1.5, 4.5]], 3),
    # ([[1.5, 4.5], [0, 5]], 3),
    # ([[0, 5], [1.5, 4.5], [1, 8]], 4),
    # ([[0, 5], [4, 8]], 1),
    # ([[0, 5], [5, 8]], 0),
    # ([[0, 5.5], [2, 4], [5, 6]], 2.5),
    # ([[0, 7], [2, 4], [5, 6], [5.5, 8]], 4),
    ([[2, 5], [4, 7], [6, 9]], 2),
]


@pytest.mark.parametrize("segments, length", segs)
def test_horizontal_sweep(segments, length):
    heapq.heapify(segments)
    height = horizontal_sweep(segments)
    print(height)
    assert height == length


def test_horizontal_sweep_2():
    with open("rectangles.json", "r") as jin:
        all_recs = json.load(jin)
    # print(all_recs)

    rects = build_rectangles(all_recs["r5"]["rec"])
    for r in rects:
        print(r)

    events = build_events(rects, horizontal=True)
    for e in events:
        print(e)

    # active = {rects[0], rects[1], rects[2], rects[3]}
    # active = {rects[0], rects[1]}
    # active = {rects[0], rects[1], rects[2]}
    active = {rects[1], rects[2], rects[3]}
    height = horizontal_sweep2(events, active)
    print(height)
