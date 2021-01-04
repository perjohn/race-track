from mock import patch

import numpy as np

from main import RaceTrackEpisodeGenerator
from tests.test_tracks import TEST_TRACK_GRID
from tracks import Track


@patch('main.random.randint')
def test_generate_episode(mock_randint):
    mock_randint.side_effect = [0, 2, 0, 0, 0, 0]
    episode_generator = RaceTrackEpisodeGenerator(Track(TEST_TRACK_GRID))
    result = episode_generator.generate_episode()
    assert len(result) == 9
    assert result[-1] == 0


@patch('main.random.randint')
def test_generate_episode_return_to_start(mock_randint):
    mock_randint.side_effect = [0, 1, 0, 0, 0, 2, 0, 0, 0, 0]
    episode_generator = RaceTrackEpisodeGenerator(Track(TEST_TRACK_GRID))
    result = episode_generator.generate_episode()
    assert len(result) == 18
    assert result[-1] == 0


@patch('main.random.randint')
def test_generate_episode_return_to_start_outside_of_grip(mock_randint):
    TEST_TRACK_GRID = np.array([
        [-1, -1, -1, -1],
        [-1, 1, 1, -1],
        [-1, 0, 0, -1],
        [-1, 0, 0, -1],
        [-1, 2, 2, -1],
        [-1, -1, -1, -1],
    ])

    mock_randint.side_effect = [0, 1, 1, 0, 2, 0, 0]
    episode_generator = RaceTrackEpisodeGenerator(Track(TEST_TRACK_GRID))
    result = episode_generator.generate_episode()
    assert len(result) == 15
    assert result[-1] == 0


@patch('main.random.randint')
def test_valid_actions(mock_randint):
    mock_randint.return_value = 0
    episode_generator = RaceTrackEpisodeGenerator(Track(TEST_TRACK_GRID))
    result = episode_generator._choose_action()
    assert result == (0, 0)
