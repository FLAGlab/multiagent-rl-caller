import unittest
from environment.core import Survey, Study, World


class TestSurvey(unittest.TestCase):
    def setUp(self):
        self.survey = Survey(0, 2, 20, True)

    def test_creation(self):
        self.assertFalse(self.survey.complete)


class TestStudy(unittest.TestCase):

    def setUp(self):
        self.survey = Survey(0, 2, 20, True)
        self.study = Study(1, 3)

    def test_add_survey(self):
        self.study.add_survey(2, 20, True)
        self.assertEqual(len(self.study.surveys), 1)
        self.assertEqual(self.study.surveys[-1], self.survey)

    def test_get_surveys(self):
        self.study.add_survey(2, 20, True)
        self.study.add_survey(4, 23, True)
        self.assertEqual(len(self.study.get_surveys(2, 20, True)), 1)
        self.assertEqual(self.study.get_surveys(2, 20, True)[-1], self.survey)

    def test_get_empty_surveys_subset(self):
        self.study.add_survey(2, 20, True)
        self.study.add_survey(4, 23, True)
        self.assertEqual(len(self.study.get_surveys(4, 20, True)), 0)

    def test_complete_survey(self):
        self.study.add_survey(2, 20, True)
        self.study.add_survey(4, 23, True)
        self.study.complete_survey(0)
        self.assertEqual(len(self.study.get_surveys(2, 20, True)), 0)


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.world = World()
        self.study = Study(1, 3)

    def test_add_study(self):
        self.world.add_study(self.study)
        self.assertEqual(self.world.num_studies, 1)
        self.assertEqual(self.world.studies[-1], self.study)
