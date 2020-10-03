OPEN = 1
CLOSE = 0


def horizontal(segments):
    low_boundary = None
    high_boundary = None
    low_inside = float("inf")
    high_inside = float("-inf")

    sums = []
    segments.sort(key=lambda x: x[0])
    low_boundary, high_boundary = segments[0]
    updated = False
    for i in range(1, len(segments)):
        low, high = segments[i]
        # totally inside
        if low >= low_boundary and high <= high_boundary:
            low_inside = min(low_inside, low)
            high_inside = max(high_inside, high)
            updated = True
            print("inside")
        # overlap
        elif low <= high_boundary < high:
            low_inside = low
            high_inside = high_boundary
            high_boundary = high
            updated = True
            print("overlap")
        # no overlap
        elif low > high_boundary:
            print("no overlap")

        if updated:
            temp = high_inside - low_inside
            sums.append(temp)
            print(temp, sums)
            updated = False

    return sum(sums)


def horizontal_sweep3(segments):
    if not segments:
        return 0

    events = []
    for idx, seg in enumerate(segments):
        # store id and endpoint
        events.append((OPEN, idx, seg[0]))
        events.append((CLOSE, idx, seg[1]))
    events.sort(key=lambda x: x[2])
    print(events)

    laps = []
    segs = {}

    for typ, sid, pt in events:
        if typ == OPEN:
            segs[sid] = pt

        else:
            segs[sid] = pt - segs[sid]
    return sum(laps)

    cur_bot = events[0][1]
    cur_top = events[0][2]
    laps = []
    for typ, bot, top in events:
        if typ == OPEN:
            cur_bot = bot
        else:
            cur_top = top
            olap = cur_top - cur_bot
            laps.append(olap)
    print(olap)


def klees(segments):
    if not segments:
        return 0
    events = []
    for seg in segments:
        # store id and endpoint
        events.append((OPEN, seg[0]))
        events.append((CLOSE, seg[1]))
    events.sort(key=lambda x: x[1])
    result = 0
    count = 0
    for i in range(len(events)):
        prev = events[i - 1]
        cur = events[i]
        if i > 0 and cur[1] > prev[1] and count > 0:
            result += cur[1] - prev[1]
        if cur[0] == OPEN:
            count += 1
        else:
            count -= 1
    print(result)
    return result
