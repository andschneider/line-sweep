from globals import START


def horizontal_sweep(events, active):
    total = 0
    if not active:
        return total

    count = 0  # how many are overlapping
    sums = []
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
                sums.append(delta_y)
    # print(sums)
    return sum(sums)
