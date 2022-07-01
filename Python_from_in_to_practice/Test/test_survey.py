from http.client import responses
import unittest
from survey import AnonymousSurvey

class TestAnonyousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language ..."
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn('English',my_survey.responses)
        
    def test_store_Three_response(self):
        question = "What language ..."
        my_survey = AnonymousSurvey(question) # 可用setUp简化:q
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        self.assertIn('English',my_survey.responses)

if __name__ == '__main__':
    unittest.main()