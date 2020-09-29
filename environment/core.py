import numpy as np


class Survey():
    def __init__(self, id, socioeconomic, age, urban):
        self.id = id
        self.complete = False
        self.socioeconomic = socioeconomic
        self.age = age
        self.is_urban = urban

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

    def add_survey(self, socioeconomic, age, urban):
        if self.num_surveys > len(self.surveys):
            survey = Survey(len(self.surveys), socioeconomic=socioeconomic, age=age, urban=urban)
            self.surveys = np.append(self.surveys, survey)


class Agent():
    def __init__(self, id):
        self.id = id


class World():
    def __init__(self):
        self.num_studies = None
        self.studies = None
