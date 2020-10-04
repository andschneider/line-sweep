# line sweep

## Overview

This is a double line sweep algorithm for calculating the intersection area of rectangles.

The two sweeps performed are one going left to right, and one going bottom to top. The left to right sweep is the main sweep and it processes the vertical edges of each rectangle. When a left edge is encountered it sets that rectangle as "active" and adds it to an active set. When a right edge is encountered, the rectangle is removed from the active set.

After each vertical edge gets processed (either added or removed from the active set), the horizontal sweep is ran. It calculates the total intersection length of the currently overlapping active rectangles.

The area can be calculated by simply multiplying the horizontal sweep result with the distance between two vertical events. The total area is then the summation of all these "event areas".

For more indepth explanations, see the links in the __Resources__ section below.

## Set up

1) pip install the dependencies in the `requirements.txt` file with `pip install -r requirements.txt` (preferably in a virtual environment).

2) set the correct Python runtime in the `Makefile`. Right now it's set as `python` but might need to be `python3` depending on your system.

## Running

To run the algorithm, run `make test-solution`. This will run through all the test rectangles defined in the `rectangles.json` file, which can be found in the `tests/data` directory.
 
### plotting

I found it helpful to plot the rectangles and visually check their intersection areas.

To plot all the test rectangles, run `make plots`. This will plot each set of rectangles in their own browser tab using Plotly.

## Resources

Some helpful resources I used. Lots of credit goes to the first link.

- https://www.hackerearth.com/practice/math/geometry/line-sweep-technique/tutorial/
- https://leetcode.com/problems/rectangle-area-ii/
- https://youtu.be/p9cChQlgx08
- https://plotly.com/python/shapes/
