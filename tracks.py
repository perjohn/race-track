import random

import numpy as np

START = 1
END = 2


class Track:
    def __init__(self, track_grid):
        self.track_grid = track_grid
        self.start_states = self._get_start_states()
        self.finish_states = self._get_finish_states()
        self.grid_width = track_grid.shape[1]
        self.grid_height = track_grid.shape[0]

    def _get_start_states(self):
        indexes = np.where(self.track_grid == START)
        return [(row, col) for row, col in zip(indexes[0], indexes[1])]

    def get_random_start_position(self) -> tuple:
        rand_idx = random.randint(0, len(self.start_states) - 1)
        return self.start_states[rand_idx]

    def _get_finish_states(self):
        indexes = np.where(self.track_grid == END)
        return [(row, col) for row, col in zip(indexes[0], indexes[1])]


def track1() -> np.ndarray:
    track = np.zeros((34, 19), dtype=np.int8)
    track[0, :] = -1
    track[1:4, 0:4] = -1
    track[4:11, 0:3] = -1
    track[11:19, 0:2] = -1
    track[19:29, 0] = -1
    track[29, 0:2] = -1
    track[30:32, 0:3] = -1
    track[32, 0:4] = -1
    track[33, :] = -1
    track[1:26, 10:19] = -1
    track[26, 11:19] = -1
    track[27:33, 18] = -1
    track[1, 4:10] = START  # start states
    track[27:33, 17] = END  # end states
    return track
