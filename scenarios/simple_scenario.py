from environment.core import World, Study
import environment.core as core


class Scenario():
    def make_world(self):
        world = World()
        politica = Study(1, 100)
        medios = Study(2, 180)
        covid = Study(3, 360)

        for i in range(50):
            politica.add_survey(3, core.JOVENES)

        for i in range(25):
            politica.add_survey(4, core.ADULTOS)
            politica.add_survey(5, core.ADULTOS_MAYORES)

        for i in range(10):
            for j in range(1, 7):
                medios.add_survey(j, core.ADOLECENETES)
                medios.add_survey(j, core.ADULTOS)
                medios.add_survey(j, core.ADULTOS_MAYORES)

        for i in range(10):
            for j in range(1, 7):
                for k in [True, False]:
                    covid.add_survey(j, core.ADOLECENETES, k)
                    covid.add_survey(j, core.ADULTOS, k)
                    covid.add_survey(j, core.ADULTOS_MAYORES, k)

        world.add_study(politica)
        world.add_study(medios)
        world.add_study(covid)
        return world

    def reset_world(self, world):
        world.clean()
        politica = Study(1, 100)
        medios = Study(2, 180)
        covid = Study(3, 360)

        for i in range(50):
            politica.add_survey(3, core.JOVENES)

        for i in range(25):
            politica.add_survey(4, core.ADULTOS)
            politica.add_survey(5, core.ADULTOS_MAYORES)

        for i in range(10):
            for j in range(1, 7):
                medios.add_survey(j, core.ADOLECENETES)
                medios.add_survey(j, core.ADULTOS)
                medios.add_survey(j, core.ADULTOS_MAYORES)

        for i in range(10):
            for j in range(1, 7):
                for k in [True, False]:
                    covid.add_survey(j, core.ADOLECENETES, k)
                    covid.add_survey(j, core.ADULTOS, k)
                    covid.add_survey(j, core.ADULTOS_MAYORES, k)

        world.add_study(politica)
        world.add_study(medios)
        world.add_study(covid)

    # def reward(self, agent, world):
