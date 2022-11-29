from mesa import Agent


class MissingPerson(Agent):
    """A person that gets missing in the mountains."""

    def __init__(self, position, depth, unique_id, georesq=False):
        super().__init__(position, depth)
        self.unique_id = unique_id
        self.position = position
        self.depth = depth
        self.found = False
        self.georesq = georesq