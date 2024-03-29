from mesa import Agent


class Environment(Agent):
    def __init__(self, pos, altitude, path, model):
        super().__init__(pos, model)
        self.pos = pos
        self.altitude = altitude
        self.path = path  # presence of a path
        self.model = model

