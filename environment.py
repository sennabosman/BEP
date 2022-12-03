from mesa import Agent


class Environment(Agent):
    def __init__(self, pos, slope_1, slope_2, slope_3, path, model):
        super().__init__(pos, model)
        self.slope_1 = slope_1
        self.slope_2 = slope_2
        self.slope_3 = slope_3
        self.path = path
        self.model = model
