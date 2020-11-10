import unittest
import copy

from environment.env import Env
from scenarios.simple_scenario import Scenario


class TestEnv(unittest.TestCase):
    def setUp(self):
        self.scenario = Scenario()
        self.world = self.scenario.make_world()

    def test_creation(self):
        env = Env(scenario=self.scenario, world=self.world)
        self.assertEqual(self.world, env.world)

    def test_reset(self):
        world2 = copy.copy(self.world)
        self.scenario.reset_world(self.world)
        print(world2.studies, self.world.studies)
        self.assertEqual(world2, self.world)
