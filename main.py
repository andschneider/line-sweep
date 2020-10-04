import json
from dataclasses import dataclass
import heapq

from horizontal import horizontal_sweep, horizontal_sweep2
from primitives import Rectangle, tuple_to_rect

START, END = 0, 1


@dataclass
class Event:
    typ: int  # START or END
    point: int
    rec: Rectangle

    def __lt__(self, other):
        return self.point <= other.point

    def __repr__(self):
        t_map = {START: "start", END: "end"}  # for nicer printing
        return f"typ: {t_map[self.typ]}, pt: {self.point}"


def build_rectangles(rectangles):
    return [tuple_to_rect(r) for r in rectangles]


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


def calc_area(events, horz_events):
    area = 0
    # vertical_ranges = []
    # get first x coordinate
    prev_x = events[0].point
    # keep track of the total vertical length of intersections at an event point
    overlap_height = 0
    active = set()
    # sweep left to right with vertical sweep line
    for event in events:
        length = event.point - prev_x
        area += length * overlap_height

        # vert_range = event.rec.y_segment
        if event.typ == START:
            active.add(event.rec)
            # insert into heap based on the lowest y value in the range to remove the need for sorting later
            # O(log n) for inserts
            # heapq.heappush(vertical_ranges, Event(START, vert_range[0], event.rec))
            # heapq.heappush(vertical_ranges, Event(END, vert_range[1], event.rec))
            # heapq.heappush(vertical_ranges, vert_range)
        else:
            active.remove(event.rec)
            # need to heapify again after remove
            # vertical_ranges.remove(vert_range)
            # O(n) for heapify
            # heapq.heapify(vertical_ranges)

        # sweep bot to top with horizontal sweep line
        # overlap_height = horizontal_sweep(vertical_ranges)
        overlap_height = horizontal_sweep2(horz_events, active)
        prev_x = event.point
    return area


if __name__ == "__main__":
    # r1 = ((0, 0), (5, 5))
    # r2 = ((7, 1), (1, 8))
    # r3 = ((-1, 4.5), (5.5, 1.5))

    # r1 = ((0, 0), (7, 7))
    # r2 = ((-1, 1), (4, 2))
    # r3 = ((1, 6), (6, 4))

    # r1 = ((2, 2), (6, 1))
    # r2 = ((4, 4), (12, -1))
    # r3 = ((8, 2), (14, 1))
    # recs = [r1, r2, r3]

    # r1 = ((2, 2), (5, 0))
    # r2 = ((3, 1), (6, 4))
    # recs = [r1, r2]

    # r1 = ((0, 0), (5, 5))
    # r2 = ((2, 2), (4, 6))
    # recs = [r1, r2]

    # r1 = ((-4, -1), (-1, 1))
    # r2 = ((-2, 2), (1, 4))
    # r3 = ((-1.5, 6), (4, 5))
    # r4 = ((0, 7), (7, 0))
    # recs = [r1, r2, r3, r4]

    # r1 = ((-1, 4), (8, 7))
    # r2 = ((4, 5), (14, 2))
    # r3 = ((6, 9), (16, 6))
    # r4 = ((10, 1), (12, 11))
    # recs = [r1, r2, r3]
    # recs = [r1, r2, r3, r4]

    with open("rectangles.json", "r") as jin:
        all_recs = json.load(jin)

    for i in range(1, 8):
        rectangle = f"r{i}"
        coords = all_recs[rectangle]["rec"]
        ans = all_recs[rectangle]["ans"]
        rects = build_rectangles(coords)
        # for r in rects:
        #     print(r)

        events = build_events(rects)
        # for e in events:
        #     print(e)

        hevents = build_events(rects, horizontal=True)

        area = calc_area(events, hevents)
        print(rectangle, area, ans)
        assert area == ans
