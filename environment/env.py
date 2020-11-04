# from .core import World
# import numpy as np


class Env():

    def __init__(self, scenario, world):
        self.scenario = scenario
        self.world = world
        # set world using defined scenario
        # self.scenario.reset_world(self.world)
