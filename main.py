import mesa
from drone import Drone
from mountain import Mountain
from missing_person import MissingPerson
from environment import Environment


def agent_portrayal(agent):
    """This function defines the colors of the different agents."""
    portrayal = {"Shape": "circle", "Color": "red", "Filled": "true", "Layer": 0, "r": 0.8}

    if type(agent) is Environment:
        if agent.slope_1 is True:
            portrayal["Color"] = "lightgray"
        elif agent.slope_2 is True:
            portrayal["Color"] = "darkgrey"
        elif agent.slope_3 is True:
            portrayal["Color"] = "dimgrey"

    elif type(agent) is Drone:
        portrayal["Color"] = "blue"

    elif type(agent) is MissingPerson:
        if agent.found:
            portrayal["Color"] = "green"

    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 100, 100, 500, 500)
server = mesa.visualization.ModularServer(Mountain, [grid], "Mountain", {"width": 100, "height": 100})
server.port = 8521
server.launch()


"""--------------------------
area = 63 km x 63 km
pixel = 50 m x 50 m
grid = 1285 pixel x 1285 pixel
---------------------------"""