from models import Mountain, Drone, MissingPerson
import mesa


def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": "red",
        "Filled": "true",
        "Layer": 0,
        "r": 0.8
    }

    if type(agent) is Drone:
        portrayal["Color"] = "blue"

    elif type(agent) is MissingPerson:
        if agent.found:
            portrayal["Color"] = "green"

    return portrayal



grid = mesa.visualization.CanvasGrid(agent_portrayal, 100, 100, 500, 500)
server = mesa.visualization.ModularServer(Mountain, [grid], "Mountain", {"width": 100, "height": 100})
server.port = 8521
server.launch()

