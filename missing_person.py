from mesa import Agent
import random
from utils import get_height_map

class MissingPerson(Agent):
    """A person that gets missing in the mountains."""
    def __init__(self, unique_id, x, y, model, path, georesq=False, avalanche=False):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.x = x
        self.y = y
        self.height = 0
        self.georesq = georesq
        self.avalanche = avalanche
        self.path = path
        self.heightmap = get_height_map()

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

    def walk_height(self, new_position):
        current_height = self.height
        index = ((99 - new_position[0]) * 100) + new_position[1]
        next_height = self.heightmap[index][2]
        difference = next_height - current_height
        if difference > 0:
            if self.path:
                self.speed = 0.0309
            else:
                self.speed = 0.0247
        elif difference == 0:
            if self.path:
                self.speed = 0.0463
            else:
                self.speed = 0.0370
        else:
            if self.path:
                self.speed = 0.0618
            else:
                self.speed = 0.0494
        self.height = next_height

    def move_path(self):
        end = (64, 88)
        position = self.xy_to_cell()
        x, y = position
        x_end, y_end = end
        dx = abs(x - x_end)
        dy = abs(y - y_end)

        if dy > dx:
            if (y_end - y) > 0:
                self.y += self.speed
            else:
                self.y -= self.speed

        elif dx > dy:
            if (x_end - x) > 0:
                self.x += self.speed
            else:
                self.x -= self.speed

        else:
            if (x_end - x) > 0:
                self.x += self.speed
            else:
                self.x -= self.speed
            if (y_end - y) > 0:
                self.y += self.speed
            else:
                self.y -= self.speed

    def move_random(self):
        """This function determines the random walking behaviour of the missing person."""
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
        if self.path:
            self.move_path()
            cell = self.xy_to_cell()
            self.walk_height(cell)
            self.model.grid.move_agent(self, cell)
        else:
            if self.avalanche is False:  # if there is no avalanche, the agent can move
                self.move_random()
                cell = self.xy_to_cell()
                self.walk_height(cell)
                self.model.grid.move_agent(self, cell)

