from dataclasses import dataclass

from globals import START, END
from primitives import Rectangle


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


def build_events(rectangles, horizontal=False):
    events = []
    for r in rectangles:
        if horizontal:
            events.append(Event(START, r.c1.y, r))
            events.append(Event(END, r.c2.y, r))
        else:
            events.append(Event(START, r.c1.x, r))
            events.append(Event(END, r.c2.x, r))
    # sort by point
    events.sort()
    return events
