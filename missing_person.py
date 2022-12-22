from mesa import Agent
import random


class MissingPerson(Agent):
    """A person that gets missing in the mountains."""
    def __init__(self, unique_id, x, y, model, georesq=False, avalanche=False, path=False):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.x = x
        self.y = y
        self.georesq = georesq
        self.avalanche = avalanche
        self.path = path

        self.found = False

        if self.path:
            self.speed = 0.0463  # if the agent is walking on a track, the speed is 0.0463 cells per model step
        else:
            self.speed = 0.0370  # if the agent is walking off track, the speed is 0.0370 cells per model step

    def xy_to_cell(self):
        """This function converts the float position of the missing person to integer coordinates of a cell."""
        x = int(self.x)
        y = int(self.y)
        return x, y

    def move(self):
        """This function determines the walking behaviour of the missing person."""
        current_cell = self.xy_to_cell()
        if current_cell == (0, 0):  # if agent is in left bottom corner, move right and/or up
            self.x += self.speed * random.choice([0, 1])
            self.y += self.speed * random.choice([0, 1])
        elif current_cell == (0, 99):  # if agent is in left top corner, move right and/or down
            self.x += self.speed * random.choice([0, 1])
            self.y -= self.speed * random.choice([0, 1])
        elif current_cell == (99, 0):  # if agent is in right bottom corner, move left and/or up
            self.x -= self.speed * random.choice([0, 1])
            self.y += self.speed * random.choice([0, 1])
        elif current_cell == (99, 99):  # if agent is in right top corner, move left and/or down
            self.x -= self.speed * random.choice([0, 1])
            self.y -= self.speed * random.choice([0, 1])
        elif current_cell == (0, self.y):  # if agent is at left border, move right and/or up or down
            self.x += self.speed * random.choice([0, 1])
            self.y += self.speed * random.choice([-1, 0, 1])
        elif current_cell == (self.x, 0):  # if agent is at bottom border, move up and/or left or right
            self.x += self.speed * random.choice([-1, 0, 1])
            self.y += self.speed * random.choice([0, 1])
        elif current_cell == (99, self.y):  # if agent is at right border, move left and/or up or down
            self.x -= self.speed * random.choice([0, 1])
            self.y += self.speed * random.choice([-1, 0, 1])
        elif current_cell == (self.x, 99):  # if agent is at top border, move down and/or left or right
            self.x += self.speed * random.choice([-1, 0, 1])
            self.y -= self.speed * random.choice([0, 1])
        else:  # if agent is in middle of grid, move random
            possible_steps = [-1, 0, 1]
            self.x += self.speed * random.choice(possible_steps)
            self.y += self.speed * random.choice(possible_steps)

    def step(self):
        positions = []
        if self.avalanche is False:  # if there is no avalanche, the agent can move
            self.move()
            cell = self.xy_to_cell()
            positions.append(cell)
            self.model.grid.move_agent(self, cell)