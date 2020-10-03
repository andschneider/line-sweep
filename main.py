from horizontal import horizontal_sweep, horizontal
from primitives import Rectangle, tuple_to_rect
from typing import List, Tuple
from dataclasses import dataclass
import heapq


def build_rectangles(rects):
    return [tuple_to_rect(r) for r in rects]


OPEN, CLOSE = 0, 1
START, END = 0, 1
VERT, HORZ = 0, 1


@dataclass
class Event2:
    typ: int  # OPEN or CLOSE
    dir: int  # VERT or HORZ
    rec: Rectangle

    def __repr__(self):
        if self.typ == START:
            t = "open"
        else:
            t = "close"
        return f"typ: {t}, pt: {self.dir}, rec: {self.rec}"


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
        return f"typ: {t}, pt: {self.point}"
        # return f"typ: {t}, pt: {self.point}, rec: {self.rec}"


def build_events(rects, horizontal=False):
    events = []
    for r in rects:
        if horizontal:
            events.append(Event(START, r.c1.y, r))
            events.append(Event(END, r.c2.y, r))
        else:
            events.append(Event(START, r.c1.x, r))
            events.append(Event(END, r.c2.x, r))
    # sort by point
    events.sort(key=lambda x: x.point)
    return events


from collections import deque


# TODO this doesn't work
def horizontal_sweep2(segments):
    # x1 to x2 and to x3
    segments.sort()
    xlaps = []
    prev = segments[0]
    # for cur in segments:
    for i in range(1, len(segments)):
        cur = segments[i]
        # prev = segments[i-1]
        if cur[0] <= prev[1]:
            # completely contained
            if cur[1] < prev[1]:
                olap = cur[1] - cur[0]
            # overlap
            else:
                olap = prev[1] - cur[0]
                prev = [cur[0], prev[1]]
            xlaps.append(olap)
    print(xlaps)
    return sum(xlaps)
    # segments.sort()
    # top = segments[0][1]
    # height = segments[0][1] - segments[0][0]
    # for b, t in segments:
    #     if b < top < t:
    #         height += t - top
    #         top = t
    #
    #     if b >= top:
    #         height += t - b
    #         top = t
    #
    # return height


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


def merge_interval(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    total = intervals[0][1] - intervals[0][0]
    for l, r in intervals:
        if l < end and r > end:
            total += r - end
            end = r

        if l >= end:
            total += r - l
            end = r

    return total


if __name__ == "__main__":
    r1 = ((0, 0), (5, 5))
    r2 = ((7, 1), (1, 8))
    r3 = ((-1, 4.5), (5.5, 1.5))

    rects = build_rectangles([r1, r2, r3])
    for rect in rects:
        print(rect)

    # vertical edges
    e = build_events(rects)
    # for ee in e:
    #     print(ee)
    # horizontal edges
    # eh = build_events(rects, horizontal=True)
    # for ee in eh:
    #     print(ee)

    area = 0
    segments = []
    horz_events = {}
    # get first x coordinate
    prev_x = e[0].point
    intersect_height = 0
    # sweep left to right
    for event in e:
        length = event.point - prev_x
        area += length * intersect_height
        rectangle = event.rec
        if event.typ == OPEN:
            # segments.append(Event2(START, HORZ, event.rec))
            segments.append(event.rec.y_segment)
            horz_events[rectangle] = [
                Event(START, rectangle.c1.y, rectangle),
                Event(END, rectangle.c2.y, rectangle),
            ]
        else:
            del horz_events[rectangle]
            segments.remove(event.rec.y_segment)

        # print(horz_events)
        # ih2 = horizontal_sweep(horz_events)
        # ih = calc_overlap(segments)
        intersect_height = horizontal(segments)
        # print(intersect_height, ih, ih2)
        prev_x = event.point

    print(area)
