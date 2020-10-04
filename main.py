import json

from events import build_events
from globals import START
from horizontal import horizontal_sweep
from primitives import tuple_to_rect


def build_rectangles(rectangles):
    return [tuple_to_rect(r) for r in rectangles]


def calc_area(vert_events, horz_events):
    area = 0
    # get first x coordinate
    prev_x = vert_events[0].point
    # keep track of the total vertical length of intersections at an event point
    overlap_height = 0
    active = set()
    # sweep left to right with vertical sweep line
    for event in vert_events:
        length = event.point - prev_x
        area += length * overlap_height

        if event.typ == START:
            active.add(event.rec)
        else:
            active.remove(event.rec)

        # sweep bot to top with horizontal sweep line
        overlap_height = horizontal_sweep(horz_events, active)
        prev_x = event.point
    return area


if __name__ == "__main__":
    with open("rectangles.json", "r") as jin:
        all_recs = json.load(jin)

    for i in range(1, 13):
        rectangle = f"r{i}"
        coords = all_recs[rectangle]["rec"]
        ans = all_recs[rectangle]["ans"]
        rects = build_rectangles(coords)
        # for r in rects:
        #     print(r)

        vevents = build_events(rects)
        # for e in events:
        #     print(e)

        hevents = build_events(rects, horizontal=True)

        area = calc_area(vevents, hevents)
        print(rectangle, area, ans)
        assert area == ans
