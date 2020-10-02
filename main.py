from primitives import Rectangle, tuple_to_rect
from typing import List, Tuple
from dataclasses import dataclass
import heapq


def build_rectangles(rects):
    return [tuple_to_rect(r) for r in rects]


OPEN, CLOSE = 0, 1


@dataclass
class Event:
    typ: int  # OPEN or CLOSE
    point: int
    rec: Rectangle

    def __repr__(self):
        if self.typ == OPEN:
            t = "open"
        else:
            t = "close"
        return f"typ: {t}, pt: {self.rec}, rec: {self.rec}"


def build_events(rects):
    events = []
    for r in rects:
        events.append(Event(OPEN, r.c1.x, r))
        events.append(Event(CLOSE, r.c2.x, r))
    # sort by x
    events.sort(key=lambda x: x.point)
    return events


# TODO this doesn't work
def horizontal_sweep(segments):
    segments.sort()
    top = segments[0][1]
    height = segments[0][1] - segments[0][0]
    for b, t in segments:
        if b < top < t:
            height += t - top
            top = t

        if b >= top:
            height += t - b
            top = t

    return height


def calc_overlap(segments):
    """Calculates the overlap of colinear line segments."""
    if not segments:
        return 0

    upper = []  # max heap
    lower = []  # min heap

    # add
    for bot, top in segments:
        heapq.heappush(upper, -top)  # negate to make max heap
        heapq.heappush(lower, bot)

    # remove largest and smallest (boundary points)
    heapq.heappop(upper)
    heapq.heappop(lower)

    # the second largest and second smallest represent
    if upper and lower:
        return -upper[0] - lower[0]
    return 0


if __name__ == '__main__':
    r1 = ((0, 0), (5, 5))
    r2 = ((7, 1), (1, 8))
    r3 = ((-1, 4.5), (5.5, 1.5))

    rects = build_rectangles([r1, r2, r3])
    # for rect in rects:
    #     print(rect)

    e = build_events(rects)

    area = 0
    segments = []
    prev_x = e[0].point
    height = 0
    # sweep left to right
    count = 0
    for event in e:
        length = event.point - prev_x
        area += length * height
        if event.typ == OPEN:
            segments.append(event.rec.y_segment)
        else:
            segments.remove(event.rec.y_segment)

        height = calc_overlap(segments)
        prev_x = event.point

    print(area)
