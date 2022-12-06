from mesa import Agent
from utils import found_person, battery_decrement, finding_radius
from variables import visibility, wind, temperature


class Drone(Agent):
    """A drone that searches for the missing person."""

    def __init__(self, position, model, unique_id, person):
        super().__init__(position, model)
        self.unique_id = unique_id
        self.position = position
        self.person = person
        self.battery = 1
        self.finding_radius = finding_radius(visibility)

        self.step_nr = 0
        self.right = False
        self.down = False
        self.up = True

    def parallel_sweep_search(self):
        """A search pattern that searches for the missing person in parallel lines."""

        x, y = self.pos
        max_y = self.model.width - 2 * self.finding_radius
        steps_right = self.finding_radius

        if self.down is True and self.right is True and self.step_nr == steps_right:
            self.right = False
            self.down = False
            self.up = True
            self.step_nr = 0

        if self.up is True and self.right is True and self.step_nr == steps_right:
            self.right = False
            self.down = True
            self.up = False
            self.step_nr = 0

        if self.step_nr == max_y:
            self.right = True
            self.step_nr = 0

        if self.right is False:
            if self.up is True:
                new_pos = (x, y + 1)
                self.model.grid.move_agent(self, new_pos)
                self.step_nr += 1
            elif self.down is True:
                new_pos = (x, y - 1)
                self.model.grid.move_agent(self, new_pos)
                self.step_nr += 1
        else:
            new_pos = (x + 1, y)
            self.model.grid.move_agent(self, new_pos)
            self.step_nr += 1

        if found_person(self.pos, self.person.pos):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def linear_search(self):
        """A search pattern that searches for the missing person along a path."""

        if found_person(current_position, self.person.pos):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def expanding_search(self):
        """A search pattern that searches for the missing person from its last known location."""

        if found_person(current_position, self.person.pos):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def step(self):
        self.battery -= battery_decrement(wind, temperature)
        if self.battery > 0:
            if self.person.georesq:
                self.expanding_search()
            elif self.person.path:
                self.linear_search()
            else:
                self.parallel_sweep_search()

        else:
            print("Drone out of battery... Please charge!")
            self.model.running = False
