from FizzBuzzSolution import FizzBuzz_Solver
import unittest


class TestFizzBuzzSolver(unittest.TestCase):
    def test_FizzBuzz_10(self): #Testing up to 10 numbers
        self.assertEqual(FizzBuzz_Solver(10), [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz", "Buzz"])

    def test_FizzBuzz_15(self): #Testing up to 15 numbers
        self.assertEqual(FizzBuzz_Solver(15), [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz", "Buzz",11,"Fizz",13,14,"Fizz Buzz"])

if __name__ == "__main__":
    unittest.main()