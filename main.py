from dataclasses import dataclass
import heapq

from horizontal import horizontal_sweep
from primitives import Rectangle, tuple_to_rect

START, END = 0, 1


@dataclass
class Event:
    typ: int  # START or END
    point: int
    rec: Rectangle

    def __repr__(self):
        t_map = {START: "start", END: "end"}  # for nicer printing
        return f"typ: {t_map[self.typ]}, pt: {self.point}"


def build_rectangles(rectangles):
    return [tuple_to_rect(r) for r in rectangles]


def build_events(rectangles):
    events = []
    for r in rectangles:
        events.append(Event(START, r.c1.x, r))
        events.append(Event(END, r.c2.x, r))
    # sort by point
    events.sort(key=lambda x: x.point)
    return events


def calc_area(events):
    area = 0
    vertical_ranges = []
    # get first x coordinate
    prev_x = events[0].point
    # keep track of the total vertical length of intersections at an event point
    overlap_height = 0
    # sweep left to right with vertical sweep line
    for event in events:
        length = event.point - prev_x
        area += length * overlap_height

        vert_range = event.rec.y_segment
        if event.typ == START:
            # insert into heap based on the lowest y value in the range to remove the need for sorting later
            # O(log n) for inserts
            heapq.heappush(vertical_ranges, vert_range)
        else:
            # need to heapify again after remove
            vertical_ranges.remove(vert_range)
            # O(n) for heapify
            heapq.heapify(vertical_ranges)

        # sweep bot to top with horizontal sweep line
        overlap_height = horizontal_sweep(vertical_ranges)
        prev_x = event.point
    return area


if __name__ == "__main__":
    r1 = ((0, 0), (5, 5))
    r2 = ((7, 1), (1, 8))
    r3 = ((-1, 4.5), (5.5, 1.5))

    rects = build_rectangles([r1, r2, r3])
    for r in rects:
        print(r)

    events = build_events(rects)
    for e in events:
        print(e)

    area = calc_area(events)
    print(area)
