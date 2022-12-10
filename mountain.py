from missing_person import MissingPerson
from drone import Drone
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from utils import generate_position, finding_radius
from environment import Environment
from variables import visibility
from utils import get_height_map


class Mountain(Model):
    """A model that simulates a search and rescue process in the mountains
    with one missing person, one drone and multiple weather conditions."""

    def __init__(self, width, height):
        self.running = True
        self.width = width
        self.grid = MultiGrid(width, width, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            agent_reporters={"battery_drone": lambda battery: drone.battery})
        person_position = generate_position(width, height)
        drone_position = (finding_radius(visibility) - 1, finding_radius(visibility) - 1)
        person = MissingPerson(person_position, 0.15, self, 2)
        drone = Drone(drone_position, self, 1, person)

        self.schedule.add(drone)
        self.schedule.add(person)

        self.grid.place_agent(person, (person.position[0], person.position[1]))
        self.grid.place_agent(drone, (drone.position[0], drone.position[1]))

        height_map = get_height_map()
        i = 0
        for (contents, x, y) in self.grid.coord_iter():
            cell = Environment((x, y), height_map[i][2], False, self)
            i += 1
            self.schedule.add(cell)
            self.grid.place_agent(cell, (x, y))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, n):
        for i in range(n):
            self.step()