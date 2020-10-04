from globals import START


def horizontal_sweep(events, active):
    """Horizontal sweep line going bottom to top. If an event is in the active set of
    rectangles the rectangle will be processed.

    When the bottom edge of rectangle is encountered the count is increased, when the
    top edge is encountered it is decreased. The length of the intersection is added
    to the running sum when the count is equal to 1.
    """
    total = 0
    if not active:
        return total

    count = 0  # how many are overlapping
    length = 0  # length of intersection
    for event in events:
        if event.rec not in active:
            continue
        if event.typ == START:
            if count == 1:
                begin_y = event.rec.y_segment[0]
            count += 1
        else:
            count -= 1
            if count == 1:
                end_y = event.rec.y_segment[1]
                delta_y = end_y - begin_y
                length += delta_y
    return length
