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
        self.grid = MultiGrid(width, width, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            agent_reporters={"pos_drone": lambda drone: drone.position,
                             "battery_drone": lambda battery: drone.battery}
        )
        person_position = generate_position(width, height)
        person = MissingPerson(person_position, 0.15, 0)
        drone = Drone(generate_position(width, height), self, 1, person)

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

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        if found_person(new_position, self.person.position):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.battery -= battery_decrement(10, 20)
        if self.battery > 0:
            self.move()
        else:
            print("Drone out of battery... Please charge!")
            self.model.running = False
