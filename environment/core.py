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

    def complete_survey(self, id):
        for i in range(len(self.surveys)):
            if self.surveys[i].id == id:
                self.surveys[i].do_complete()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if len(self.surveys) == 0:
                return len(self.surveys) == len(other.surveys)
            else:
                return self.surveys == other.surveys
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Agent():
    def __init__(self, id):
        self.id = id


class World():
    def __init__(self):
        self.num_studies = None
        self.studies = np.array([])

    def add_study(self, study):
        self.studies = np.append(self.studies, study)
        self.num_studies = len(self.studies)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.num_studies == 0:
                return self.num_studies == other.num_studies
            else:
                return self.studies == other.studies
        else:
            return False
