from mesa import Agent
from mesa.model import Model

class Dirt(Agent):
    def __init__(self, unique_id: int, model: Model) -> None:
        super().__init__(unique_id, model)
        
    def step(self):
        pass
    