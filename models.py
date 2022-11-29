import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from utils import generate_position, found_person, battery_decrement

"""--------------------------
area = 63 km x 63 km
pixel = 50 m x 50 m
grid = 1285 pixel x 1285 pixel
---------------------------"""


class Mountain(Model):
    """A model that simulates a search and rescue process in the mountains
    with one missing person, one drone and multiple weather conditions."""

    def __init__(self, width, height):
        self.running = True
        self.width = width
        self.grid = MultiGrid(width, width, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            agent_reporters={"pos_drone": lambda drone: drone.position,
                             "battery_drone": lambda battery: drone.battery}
        )
        person_position = generate_position(width, height)
        drone_position = (9, 9, 0)
        person = MissingPerson(person_position, 0.15, 0)
        drone = Drone(drone_position, self, 1, person)

        self.schedule.add(drone)

        self.grid.place_agent(person, (person.position[0], person.position[1]))
        self.grid.place_agent(drone, (drone.position[0], drone.position[1]))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, n):
        for i in range(n):
            self.step()


class MissingPerson(Agent):
    """A person that gets missing in the mountains."""

    def __init__(self, position, depth, unique_id):
        super().__init__(position, depth)
        self.unique_id = unique_id
        self.position = position
        self.depth = depth
        self.found = False


class Drone(Agent):
    """A drone that searches for the missing person."""

    def __init__(self, position, model, unique_id, person, georesq=False):
        super().__init__(position, model)
        self.unique_id = unique_id
        self.position = position
        self.person = person
        self.battery = 1
        self.finding_radius = 10
        self.georesq = georesq
        self.up = True
        self.right = False
        self.down = False
        self.step_nr = 0

    def parallel_sweep_search(self):

        x, y = self.pos
        max_y = self.model.width - 2 * self.finding_radius
        steps_right = self.model.width / 10

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

        if found_person(self.pos, self.person.position):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def linear_search(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        current_position = self.pos

        if found_person(current_position, self.person.position):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def sector_search(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        current_position = self.pos

        if found_person(current_position, self.person.position):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def expanding_search(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        current_position = self.pos

        if found_person(current_position, self.person.position):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def step(self):
        self.battery -= battery_decrement(10, 20)
        if self.battery > 0:
            if self.georesq:
                self.expanding_search()
            else:
                self.parallel_sweep_search()
        else:
            print("Drone out of battery... Please charge!")
            self.model.running = False
