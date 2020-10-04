from events import build_events
from globals import START
from horizontal import horizontal_sweep
from primitives import tuple_to_rect


def build_rectangles(rectangles):
    return [tuple_to_rect(r) for r in rectangles]


def calc_area(vert_events, horz_events):
    """Calculates the total area of intersections in n rectangles.

    vert_events : List[Event]
        The vertical events, which are the left (START) and right (END) edges of a rectangle.
    horz_events : List[Event]
        The horizontal events, which are the bottom (START) and top (END) edges of a rectangle.
    """
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

        # when a left edge is found, add the rectangle to the active set
        if event.typ == START:
            active.add(event.rec)
        # when a right edge is found, it is no longer active
        else:
            active.remove(event.rec)

        # sweep bot to top with horizontal sweep line
        overlap_height = horizontal_sweep(horz_events, active)
        prev_x = event.point
    return area


def prepare_run(coordinates, verbose=False):
    """Takes in a set of coordinates and creates the rectangles and vertical and horizontal events."""
    rects = build_rectangles(coordinates)
    vevents = build_events(rects)
    hevents = build_events(rects, horizontal=True)

    if verbose:
        for r in rects:
            print(r)
        for e in vevents:
            print(e)
        for e in hevents:
            print(e)

    return vevents, hevents
