from mesa import Agent
from utils import found_person, battery_decrement, finding_radius, get_height_map


class Drone(Agent):
    """A drone that searches for the missing person."""
    def __init__(self, unique_id, x, y, model, person, params):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.x = x
        self.y = y
        self.height = 0
        self.person = person
        self.params = params

        if params['drone'] == 1:
            self.speed = 0.4630
        elif params['drone'] == 2:
            self.speed = 0.6333
        elif params['drone'] == 3:
            self.speed = 0.5
        elif params['drone'] == 4:
            self.speed = 0.8333
        elif params['drone'] == 5:
            self.speed = 0.7667
        elif params['drone'] == 6:
            self.speed = 0.5667
        elif params['drone'] == 7:
            self.speed = 0.6667

        self.battery = 1
        self.finding_radius = finding_radius(params['visibility'], params['drone'])

        self.step_nr = 0
        self.steps_dir = 0
        self.right = False
        self.left = False
        self.down = False
        self.up = True

        self.heightmap = get_height_map()


    def xy_to_cell(self):
        """This function converts the float position of the drone to integer coordinates of a cell."""
        x = int(self.x)
        y = int(self.y)
        return x, y

    def fly_height(self, new_position):
        current_height = self.height
        index = ((new_position[0]) * 100) + (new_position[1])
        next_height = self.heightmap[index][2] + (self.finding_radius * 30)
        print(current_height, next_height, index)
        difference = next_height - current_height
        if difference > 0:
            self.battery -= 0.00001 * difference  # WAARDE AANPASSEN
        self.height = next_height

    def parallel_sweep(self):
        """A search pattern that searches for the missing person in parallel lines."""

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
                self.y += self.speed
                self.step_nr += 1
            elif self.down is True:
                self.y -= self.speed
                self.step_nr += 1
        else:
            self.x += self.speed
            self.step_nr += 1

        if found_person(self.pos, self.person.pos, self.params['drone']):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def track_line(self):
        """A search pattern that searches for the missing person along a path."""

        end = (15, 20)
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

        if found_person(self.pos, self.person.pos, self.params['drone']):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

    def expanding_square(self):
        """A search pattern that searches for the missing person from its last known location."""

        if found_person(self.pos, self.person.pos, self.params['drone']):
            print("Missing person was found!")
            self.person.found = True
            self.model.running = False

        if self.steps_dir > 0:
            if self.right is True:
                self.x += self.speed
            if self.left is True:
                self.x -= self.speed
            if self.up is True:
                self.y += self.speed
            if self.down is True:
                self.y -= self.speed
            self.steps_dir -= 1
            return

        if self.step_nr % 2:
            if (self.step_nr / 2) % 2 == 0.5:
                self.right = True
                self.left = False
                self.down = False
                self.up = False
                self.x += self.speed
            else:
                self.right = False
                self.left = True
                self.down = False
                self.up = False
                self.x -= self.speed
        else:
            if (self.step_nr / 2) % 2:
                self.right = False
                self.left = False
                self.down = True
                self.up = False
                self.y -= self.speed
            else:
                self.right = False
                self.left = False
                self.down = False
                self.up = True
                self.y += self.speed
        self.step_nr += 1
        self.steps_dir = self.finding_radius * (self.step_nr / 2) - 1

    def step(self):
        self.battery -= battery_decrement(self.params['wind'], self.params['temperature'], self.params['drone'])
        if self.battery > 0:
            if self.person.georesq:
                self.expanding_square()
                cell = self.xy_to_cell()
                self.fly_height(cell)
                self.model.grid.move_agent(self, cell)
            elif self.person.path:
                self.track_line()
                cell = self.xy_to_cell()
                self.fly_height(cell)
                self.model.grid.move_agent(self, cell)
            else:
                self.parallel_sweep()
                cell = self.xy_to_cell()
                self.fly_height(cell)
                self.model.grid.move_agent(self, cell)
        else:
            print("Drone out of battery... Please charge!")
            self.model.running = False
