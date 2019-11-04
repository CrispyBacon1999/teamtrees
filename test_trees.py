import trees
import time


def test_load():
    count, curr_time = trees.load(-1, -1)
    assert count > 0
    assert curr_time <= time.time()
