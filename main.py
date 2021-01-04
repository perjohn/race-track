from collections import namedtuple
import random

from tracks import track1, Track

ACTIONS = [
    (0, 0),
    (0, 1),
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1),
]

START_VELOCITY = (0, 0)
MAX_VELOCITY_COMPONENT = 5

State = namedtuple('State', 'position velocity')


class RaceTrackEpisodeGenerator:

    def __init__(self, track: Track):
        self.track = track
        self.state = State(position=track.get_random_start_position(), velocity=START_VELOCITY)

    def generate_episode(self) -> list:
        episode = [self.state]
        finish = False
        while not finish:
            action, reward, finish = self._step()
            if not finish:
                episode.extend([action, reward, self.state])
            else:
                episode.extend([action, reward])
        return episode

    def _step(self):
        action = self._choose_action()
        next_velocity = (self.state.velocity[0] + action[0], self.state.velocity[1] + action[1])
        next_pos = (self.state.position[0] + next_velocity[0], self.state.position[1] + next_velocity[1])
        next_state = State(position=next_pos, velocity=next_velocity)
        if self._intersected_finish(next_state):
            return action, 0, True
        if self._outside_grid(next_state):
            next_state = State(position=self.track.get_random_start_position(), velocity=START_VELOCITY)
        self.state = next_state
        return action, -1, False

    def _choose_action(self):
        valid_actions = []
        for action in ACTIONS:
            velocity_result = (self.state.velocity[0] + action[0], self.state.velocity[1] + action[1])
            if 0 <= velocity_result[0] <= MAX_VELOCITY_COMPONENT and 0 <= velocity_result[1] <= MAX_VELOCITY_COMPONENT:
                valid_actions.append(action)
        return valid_actions[random.randint(0, len(valid_actions) - 1)]

    def _intersected_finish(self, next_state: State):
        path = set()
        for i in range(0, max(next_state.velocity[0], next_state.velocity[1]) + 1):
            path.add((min(self.state.position[0] + i, next_state.position[0]),
                      min(self.state.position[1] + i, next_state.position[1])))
        end_states = set(self.track.finish_states)
        if len(path.intersection(end_states)) > 0:
            return True
        return False

    def _outside_grid(self, next_state):
        if self.track.track_grid.shape[0] - 1 < next_state.position[0] \
                or self.track.track_grid.shape[1] - 1 < next_state.position[1]:
            return True
        if self.track.track_grid[next_state.position] == -1:
            return True
        return False


def main():
    episode_generator = RaceTrackEpisodeGenerator(Track(track1()))
    episode = episode_generator.generate_episode()
    print(episode)


if __name__ == '__main__':
    main()
