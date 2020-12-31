import numpy as np

from tracks import track1, Track

TEST_TRACK_GRID = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 1, 0, 1, -1],
    [-1, 0, 0, 0, -1],
    [-1, 0, 0, 0, -1],
    [-1, 2, 2, 2, -1],
    [-1, -1, -1, -1, -1],
])


def test_track():
    track = Track(TEST_TRACK_GRID)
    assert track.grid_width == 5
    assert track.grid_height == 6


def test_start_states():
    track = Track(TEST_TRACK_GRID)
    start_states = track.start_states
    assert len(start_states) == 2
    assert (1, 1) in start_states
    assert (1, 3) in start_states


def test_get_random_start_position():
    track = Track(TEST_TRACK_GRID)
    result = track.get_random_start_position()
    assert result == (1, 1) or result == (1, 3)


def test_finish_states():
    track = Track(TEST_TRACK_GRID)
    end_states = track.finish_states
    assert len(end_states) == 3
    assert (4, 1) in end_states
    assert (4, 2) in end_states
    assert (4, 3) in end_states


def test_track1():
    track = track1()
    assert track[0, 0] == -1
