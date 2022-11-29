from missing_person import MissingPerson
from drone import Drone
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from utils import generate_position


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