from primitives import Rectangle, tuple_to_rect
from typing import List, Tuple
from dataclasses import dataclass
import heapq


def build_rectangles(rects):
    return [tuple_to_rect(r) for r in rects]


OPEN, CLOSE = 0, 1
START, END = 0, 1


@dataclass
class Event2:
    typ: int  # OPEN or CLOSE
    point: int
    rec: Rectangle

    def __repr__(self):
        if self.typ == START:
            t = "open"
        else:
            t = "close"
        return f"typ: {t}, pt: {self.rec}, rec: {self.rec}"


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

    # events = {}
    # for rect in rects:
    #     events.setdefault(rect.c1.y, []).append((1, rect.c1.x, rect.c2.x)) # start this interval
    #     events.setdefault(rect.c2.y, []).append((0, rect.c1.x, rect.c2.x)) # end this interval
    #
    # events = sorted(events.items(), key=lambda x: x[0])
    # area = 0
    # intervals = [] # blist.sortedlist()
    # last_y = events[0][0]
    # width = 0
    # for y, event in events:
    #     area += width * (y - last_y)
    #
    #     for start, x1, x2 in event:
    #         print(start, x1, x2)
    #         if start:
    #             intervals.append((x1, x2))
    #         else:
    #             intervals.remove((x1, x2))
    #
    #     width = merge_interval(intervals)
    #     last_y = y
    #
    # print(area)
