from mesa import Agent
from utils import generate_position
import random
from environment import Environment


class MissingPerson(Agent):
    """A person that gets missing in the mountains."""

    def __init__(self, position, depth, model, unique_id, georesq=False, path=False):
        super().__init__(position, model)
        self.unique_id = unique_id
        self.position = position
        self.depth = depth
        self.found = False
        self.georesq = georesq
        self.path = path

    def move(self):

        (x, y) = self.pos

        if self.pos == (0, 0): #linksonder
            new_position = (x + random.choice([0, 1]), y + random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (0, 99): #linksboven
            new_position = (x + random.choice([0, 1]), y - random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (99, 0): #rechtsonder
            new_position = (x - random.choice([0, 1]), y + random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (99, 99): #rechtsboven
            new_position = (x - random.choice([0, 1]), y - random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (0, y): #links
            new_position = (x + random.choice([0, 1]), y + random.choice([-1, 0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (x, 0): #onder
            new_position = (x + random.choice([-1, 0, 1]), y + random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (99, y): #rechts
            new_position = (x - random.choice([0, 1]), y + random.choice([-1, 0, 1]))
            self.model.grid.move_agent(self, new_position)

        elif self.pos == (x, 99): #boven
            new_position = (x + random.choice([-1, 0, 1]), y - random.choice([0, 1]))
            self.model.grid.move_agent(self, new_position)

        else:
            possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
            new_position = random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()