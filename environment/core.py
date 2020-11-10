import numpy as np

# menores de 12
MENORES = 0
# 12 a 17
ADOLECENETES = 1
# 18 - 30
JOVENES = 2
# 30 - 50
ADULTOS = 3
# 50 +
ADULTOS_MAYORES = 4


class Survey():
    def __init__(self, id, socioeconomic, age, urban=True):
        self.id = id
        self.complete = False
        self.socioeconomic = socioeconomic
        self.age = age
        self.is_urban = urban

    def do_complete(self):
        self.complete = True

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Study():
    def __init__(self, id, num_surveys):
        self.id = id
        self.complete = False
        self.num_surveys = num_surveys
        self.surveys = np.array([])

    def add_survey(self, socioeconomic, age, urban=True):
        if self.num_surveys > len(self.surveys):
            survey = Survey(len(self.surveys), socioeconomic=socioeconomic, age=age, urban=urban)
            self.surveys = np.append(self.surveys, survey)

    def get_surveys(self, socioeconomic, age, urban):
        return [survey for survey in self.surveys
                if survey.socioeconomic == socioeconomic
                and survey.age == age
                and survey.is_urban == urban
                and not survey.complete]

    def summary(self):
        return None

    def complete_survey(self, id):
        for i in range(len(self.surveys)):
            if self.surveys[i].id == id:
                self.surveys[i].do_complete()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if len(self.surveys) == 0:
                return len(self.surveys) == len(other.surveys)
            else:
                return (self.surveys == other.surveys).all()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Agent():
    def __init__(self, id):
        self.id = id
        self.reward = None
        self.action = None


class World():
    def __init__(self, accept_probability=None, succes_reward=None, fail_reward=None):
        self.num_studies = 0
        self.studies = []
        self.accept_probability = accept_probability
        self.succes_reward = succes_reward

    def add_study(self, study):
        self.studies.append(study)
        self.num_studies = len(self.studies)

    def clean(self):
        self.num_studies = 0
        self.studies = []

    def step(self):
        for agent in self.agents:
            if self.accept_probability(agent) > 0.5:
                agent.reward = self.succes_reward(agent)
                self.studies[agent.action[0]].complete_survey(agent.action[1])
            else:
                agent.reward = self.fail_reward
            agent.action = None

    def observe(self):
        return [(study.id, study.summary()) for study in self.studies]

    def get_surveys(self, id_study, socioeconomic, age, urban):
        return self.studies[id_study].get_surveys(socioeconomic, age, urban)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.num_studies == 0:
                return other.num_studies == 0
            else:
                return self.studies == other.studies
        else:
            return False
