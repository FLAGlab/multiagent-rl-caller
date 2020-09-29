import unittest
from environment.core import Survey, Study

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
        self.assertEqual(len(self.study.surveys),1)
        self.assertEqual(self.study.surveys[-1], self.survey)