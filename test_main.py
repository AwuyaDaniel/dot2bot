import unittest
from main import solution
import json


file = 'data/data_1.txt'
file_2 = 'data/data_1.json'


class TestSolution(unittest.TestCase):

    def test_file(self):
        # test if the right file is being used
        message = 'File Does Not exists'

        self.assertEqual(solution(file), message)

    def test_type(self):
        # test if the right file is being used
        message = {}

        self.assertEqual(type(solution(file_2)), type(message))

