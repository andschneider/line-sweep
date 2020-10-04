from main import prepare_run, calc_area


def test_full_run(test_rectangles):
    """Test every rectangle and the area calculation."""
    print()
    print("rect   result     ans")
    for name, rectangle in test_rectangles.items():
        coords = rectangle["rec"]
        ans = rectangle["ans"]

        vert_events, horz_events = prepare_run(coords)
        area = calc_area(vert_events, horz_events)

        print(f"{name:3} {area:8} {ans:8}")
        assert area == ans
