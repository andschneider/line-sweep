def horizontal_sweep(interval_heap):
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
    total = 0
    if not interval_heap:
        return total

    low_inside = float("inf")
    high_inside = float("-inf")
    low_boundary, high_boundary = interval_heap[0]
    for i in range(1, len(interval_heap)):
        cur_l, cur_h = interval_heap[i]  # current
        prev_l, prev_h = interval_heap[i - 1]  # previous
        # no overlap
        if cur_l >= prev_h:
            print("no overlap")
            if i > 1 and low_inside < float("inf") and high_inside > float("-inf"):
                # add previous inside segment
                total += high_inside - low_inside
                # then reset lowest inside so far
                low_inside = cur_l
            # check upper boundary
            if cur_h > high_boundary:
                high_inside = high_boundary
                high_boundary = cur_h
            else:
                high_inside = cur_h
        # overlap
        else:
            low_inside = min(low_inside, cur_l)
            # totally inside
            if cur_h <= prev_h:
                print("inside")
                high_inside = max(high_inside, cur_h)
            # overlap, but only in lower portion
            elif prev_h < cur_h:
                print("overlap")
                high_inside = high_boundary
                high_boundary = cur_h
    # print(high_inside, low_inside)
    if low_inside < float("inf") and high_inside > float("-inf"):
        total += high_inside - low_inside
    return total
