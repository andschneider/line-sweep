import json
import os

import pytest


@pytest.fixture(scope="module")
def test_data_dir(request):
    """Return the path of the test data direcoty."""
    return str(request.fspath.join("..", "..", "data"))


@pytest.fixture(scope="module")
def test_rectangles(test_data_dir):
    """Read the rectangles.json from the test data dir."""
    jfile = os.path.join(test_data_dir, "rectangles.json")
    with open(jfile, "r") as jin:
        data = json.load(jin)
    return data
