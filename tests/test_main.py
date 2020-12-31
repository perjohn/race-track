from mock import patch

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
    mock_randint.side_effect = [0, 1, 0, 0, 0, 0]
    episode_generator = RaceTrackEpisodeGenerator(Track(TEST_TRACK_GRID))
    result = episode_generator.generate_episode()
    assert len(result) == 9
    assert result[-1] == 0


@patch('main.random.randint')
def test_valid_actions(mock_randint):
    mock_randint.return_value = 0
    episode_generator = RaceTrackEpisodeGenerator(Track(TEST_TRACK_GRID))
    result = episode_generator._choose_action()
    assert result == (0, 0)
