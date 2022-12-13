from mesa import Agent
import random
from environment import Environment

class MissingPerson(Agent):
    """A person that gets missing in the mountains."""

    def __init__(self, position, depth, model, unique_id, georesq=True, avalanche=False):
        super().__init__(position, model)
        self.unique_id = unique_id
        self.position = position
        self.depth = depth
        self.found = False
        self.georesq = georesq
        self.avalanche = avalanche

    def move(self):

        x, y = self.pos

        if self.pos == (0, 0):  # if agent is in left bottom corner, move right and/or up
            new_position = (x + random.choice([0, 1]), y + random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (0, 99):  # if agent is in left top corner, move right and/or down
            new_position = (x + random.choice([0, 1]), y - random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (99, 0):  # if agent is in right bottom corner, move left and/or up
            new_position = (x - random.choice([0, 1]), y + random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (99, 99):  # if agent is in right top corner, move left and/or down
            new_position = (x - random.choice([0, 1]), y - random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (0, y):  # if agent is at left border, move right and/or up or down
            new_position = (x + random.choice([0, 1]), y + random.choice([-1, 0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (x, 0):  # if agent is at bottom border, move up and/or left or right
            new_position = (x + random.choice([-1, 0, 1]), y + random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (99, y):  # if agent is at right border, move left and/or up or down
            new_position = (x - random.choice([0, 1]), y + random.choice([-1, 0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (x, 99):  # if agent is at top border, move down and/or left or right
            new_position = (x + random.choice([-1, 0, 1]), y - random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        else:  # if agent is in middle of grid, move random
            possible_steps = [-1, 0, 1]
            new_position = (x + random.choice(possible_steps), y + random.choice(possible_steps))
            self.model.grid.move_agent(self, new_position)

    def step(self):
        if self.avalanche is False:  # if there is no avalanche, agent can move
            self.move()
