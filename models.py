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
    def __init__(self, position, model, unique_id, person):
        super().__init__(position, model)
        self.unique_id = unique_id
        self.position = position
        self.person = person
        self.battery = 1
        self.finding_radius = 10

    def plowed_field_search(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        current_position = self.pos
        starting_position = self.position
        up = possible_steps[4]
        down = possible_steps[3]
        right = possible_steps[6]

        if current_position[0] == starting_position[0]:
            self.model.grid.move_agent(self, up)

        if current_position[1] == self.model.width - self.finding_radius:
            self.model.grid.move_agent(self, right)

        if current_position[1] == self.finding_radius:
            self.model.grid.move_agent(self, right)

        if found_person(current_position, self.person.position):
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
            self.plowed_field_search()
        else:
            print("Drone out of battery... Please charge!")
            self.model.running = False
