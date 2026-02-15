# Testing a function

# Unit tests and test cases

# a unit test verifies a specific aspect of a function's behave correctly
# a test case is a collection of unit tests that conclude the whole function behaves as it's supposed to

# A passing test

from surveyNemployee import Employee
import unittest
'''
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('lucas', "trinh")
        self.assertEqual(formatted_name, 'Lucas Trinh')


if __name__ == '__main__':
    unittest.main()
'''

# A class to test
from surveyNemployee import AnonSurvey
'''

ques = "What language did you first learn to speak?"
my_survey = AnonSurvey(ques)

my_survey.show_ques()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
print("thank you all for participated in this surbey!\n")
my_survey.show_results()
'''

'''
class TestAnonSurvey(unittest.TestCase):
    def test_store_single_response(self):
        ques = 'What lang did u first speak? '
        my_survey = AnonSurvey(ques)
        my_survey.store_response('ENglish')
        self.assertIn('ENglish', my_survey.responses)

    def test_store_threee_responses(self):
        ques = 'What lang did u first speak? '
        my_survey = AnonSurvey(ques)
        responses = ['English', 'Vietnamese', 'German']
        for response in responses:
            my_survey.store_response(response)
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
'''

# second way using setUp() method

'''
class TestAnonSurvey(unittest.TestCase):
    def setUp(self):
        ques = 'Languages? '
        self.my_sur = AnonSurvey(ques)
        self.responses = ['Eng', 'German', 'Viet']

    def test_store_single_respone(self):
        self.my_sur.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_sur.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_sur.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_sur.responses)


if __name__ == '__main__':
    unittest.main()
'''


# 11-3
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Lucas", 'Thai', 10000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(15000, self.my_employee.a_s)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(1)
        self.assertEqual(10001, self.my_employee.a_s)


if __name__ == '__main__':
    unittest.main()
