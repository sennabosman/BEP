from missing_person import MissingPerson
from drone import Drone
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from utils import generate_position, finding_radius
from environment import Environment
from utils import get_height_map


class Mountain(Model):
    """A model that simulates a search and rescue process in the mountains
    with one missing person, one drone and multiple weather conditions."""

    def __init__(self, width, height, visibility, wind, temperature, drone):
        self.running = True
        self.width = width
        self.grid = MultiGrid(width, width, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            agent_reporters={"battery_drone": lambda battery: drone_agent.battery,
                             "position_drone_x": lambda position_drone_x: drone_agent.x,
                             "position_drone_y": lambda position_drone_y: drone_agent.y,
                             "position_person_x": lambda position_person_x: person.x,
                             "position_person_y": lambda position_person_y: person.y}
        )

        person_position = generate_position(width, height)
        person = MissingPerson(2, person_position[0], person_position[1], self)

        finding_radius_value = finding_radius(visibility, drone)
        if person.georesq:
            drone_position = (50, 50)
        #elif person.path:
            #drone_position = (finding_radius(visibility) - 1, finding_radius(visibility) - 1)
        else:
            drone_position = (finding_radius_value - 1, finding_radius_value - 1)

        params = {
            "visibility": visibility,
            "wind": wind,
            "temperature": temperature,
            "drone": drone,
        }
        drone_agent = Drone(1, drone_position[0], drone_position[1], self, person, params)

        self.schedule.add(drone_agent)
        self.schedule.add(person)

        self.grid.place_agent(person, (person_position[0], person_position[1]))
        self.grid.place_agent(drone_agent, (drone_position[0], drone_position[1]))

        height_map = get_height_map()
        i = 0
        for (contents, x, y) in self.grid.coord_iter():
            cell = Environment((x, y), height_map[i][2], False, self)
            i += 1
            if x == person_position[0] and y == person_position[1]:
                person.height = height_map[i][2]
            if x == drone_position[0] and y == drone_position[1]:
                drone_agent.height = height_map[i][2] + (finding_radius_value * 30)
            self.grid.place_agent(cell, (x, y))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def run_model(self, n):
        for i in range(n):
            self.step()