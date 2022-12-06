from mesa import Agent


class Environment(Agent):
    def __init__(self, pos, slope_1, slope_2, slope_3, path, model):
        super().__init__(pos, model)
        self.slope_1 = slope_1  # gentle
        self.slope_2 = slope_2  # medium
        self.slope_3 = slope_3  # steep
        self.path = path  # presence of a path
        self.model = model
