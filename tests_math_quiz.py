import unittest
from math_quiz import RandomInteger_generation, Operator_generation, calculation_answer


class TestMathGame(unittest.TestCase):

    def test_RandomInteger_generation(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomInteger_generation(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Operator_generation(self):
        # TODO
        # Test if the operator is one of the expected operator
        expected_operators = ['+', '-', '*']
        for _ in range(500):  # Test a large number of random values
            operator = Operator_gereration()
            self.assertIn(operator, expected_operators)
        pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = calculation_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
            pass

if __name__ == "__main__":
    unittest.main()
