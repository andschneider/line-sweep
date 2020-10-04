import json

import plotly.graph_objects as go

from main import build_rectangles


def plot_rectangles(rectangle_dict):
    name, data = rectangle_dict
    rectangles = build_rectangles(data["rec"])

    fig = go.Figure()

    # TODO not sure why it's not picking up the ranges axes automatically
    min_x = float("inf")
    min_y = float("inf")
    max_x = float("-inf")
    max_y = float("-inf")
    for rect in rectangles:
        min_x = min(min_x, rect.c1.x)
        min_y = min(min_y, rect.c1.y)
        max_x = max(max_x, rect.c2.x)
        max_y = max(max_y, rect.c2.y)

        fig.add_shape(
            type="rect",
            x0=rect.c1.x,
            y0=rect.c1.y,
            x1=rect.c2.x,
            y1=rect.c2.y,
            line=dict(color="RoyalBlue", width=2),
            fillcolor="LightSkyBlue",
            opacity=0.2,
        )
    fig.update_layout(title=name)
    fig.update_xaxes(range=[min_x, max_x], dtick=1)
    fig.update_yaxes(range=[min_y, max_y], dtick=1)
    fig.show()


if __name__ == "__main__":
    with open("./tests/data/rectangles.json", "r") as jin:
        recs = json.load(jin)

    # This will plot all of the rectangles in their own browser tabs.
    for rectangle in recs.items():
        plot_rectangles(rectangle)
