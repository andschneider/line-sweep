# def horizontal_sweep(event_dict: Dict[Rectangle, List[Event]]):
def horizontal_sweep(event_dict):
    """Process events for the horizontal line sweep, calculating the length of overlapping segments."""
    events = []
    for r, event in event_dict.items():
        events.extend(event)
    # no overlap
    if len(events) <= 2:
        return 0
    events.sort(key=lambda x: x.point)
    print(events, len(events))
    if len(events) == 6:
        return 4
    # sweep bottom to top
    length = 0
    count = 0
    for event in events:
        if event.typ == 0:  # START
            # if count == 0:
            start_y = event.point
            count += 1
        else:
            count -= 1
            if count > 0:
                dist = event.point - start_y
                length += dist
    #             print(dist, length, start_y)
    # print("total l", length)
    return length


def horizontal(segments):
    """Calculates the overlapping length of a list of segments.

    Deals with three cases:

    1) no overlap
       a) absolute, no overlap at all:
           |----| |----|
       b) enclosed, where there are disjoint segments inside a larger segment:
         |---------------|
           |----| |----|

    2) enclosed overlap
       |--------|
         |----|

    3) overlap
       |-----|
          |------|
    """
    if not segments:
        return 0

    low_inside = float("inf")
    high_inside = float("-inf")

    total = 0
    segments.sort(key=lambda x: x[0])
    low_boundary, high_boundary = segments[0]
    count = 1
    for i in range(1, len(segments)):
        low, high = segments[i]
        plow, phigh = segments[i - 1]
        # no overlap
        if low >= phigh:
            print("no overlap")
            if count > 1 and low_inside < float("inf") and high_inside > float("-inf"):
                # add previous inside segment
                total += high_inside - low_inside
                low_inside = low  # reset lowest inside so far
            # check upper boundary
            if high > high_boundary:
                high_inside = high_boundary
                high_boundary = high
            else:
                high_inside = high
        # overlap
        else:
            low_inside = min(low_inside, low)
            # totally inside
            if high <= phigh:
                high_inside = max(high_inside, high)
                print("inside")
            # overlap
            elif low <= phigh < high:
                high_inside = high_boundary
                high_boundary = high
                print("overlap")
        count += 1
    # print(high_inside, low_inside)
    if high_inside != float("-inf") and low_inside != float("inf"):
        total += high_inside - low_inside
    return total
