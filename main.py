import mesa
import pandas as pd

from drone import Drone
from mountain import Mountain
from missing_person import MissingPerson
from environment import Environment


def agent_portrayal(agent):
    """This function defines the colors of the different agents."""
    portrayal = {"Shape": "circle", "Color": "red", "Filled": "true", "Layer": 0, "r": 0.8}

    if type(agent) is Environment:
        if agent.path:
            portrayal["Color"] = "black"
            portrayal["Layer"] = 2
        elif agent.altitude < 1800:
            portrayal["Color"] = "white"
        elif 1800 <= agent.altitude < 2000:
            portrayal["Color"] = "whitesmoke"
        elif 2000 <= agent.altitude < 2200:
            portrayal["Color"] = "gainsboro"
        elif 2200 <= agent.altitude < 2400:
            portrayal["Color"] = "lightgrey"
        elif 2400 <= agent.altitude < 2600:
            portrayal["Color"] = "silver"
        elif 2600 <= agent.altitude < 2800:
            portrayal["Color"] = "darkgrey"
        elif 2800 <= agent.altitude < 3000:
            portrayal["Color"] = "grey"
        elif agent.altitude >= 3000:
            portrayal["Color"] = "dimgrey"

    elif type(agent) is Drone:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1

    elif type(agent) is MissingPerson:
        portrayal["Layer"] = 1
        portrayal["Shape"] = "circle"
        if agent.found:
            portrayal["Color"] = "green"

    return portrayal


params = {
    "visibility": 250,
    "wind": 25,
    "temperature": 0,
    "drone": 7,
}

#grid = mesa.visualization.CanvasGrid(agent_portrayal, 100, 100, 500, 500)
#server = mesa.visualization.ModularServer(Mountain, [grid], "Mountain", {"width": 100, "height": 100, "visibility": 500, "wind": 10, "temperature": 20, "drone": 7, "path": False})
#server.port = 8521
#server.launch()

j = 1

while j < 8:
    for i in range(10):
        results = mesa.batch_run(
            Mountain,
            parameters={"width": 100, "height": 100, "visibility": 250, "wind": 25, "temperature": 0, "drone": j,
                        "path":True, "georesq":False},
            iterations=1,
            max_steps=10000,
            number_processes=1,
            data_collection_period=1,
            display_progress=True,
        )
        results_df = pd.DataFrame(results)
        results_df.to_csv(f"Data/D{j}/yespath_nogeoresq/gemiddeldweer/250_25_0_{j}_yespath_noavalanche_nogeoresq_{i}.csv")
        print(results_df)
    j += 1
