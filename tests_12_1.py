import unittest
import exm_for_tests

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = exm_for_tests.Runner('Jim')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = exm_for_tests.Runner('Jim')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = exm_for_tests.Runner('Jim')
        runner2 = exm_for_tests.Runner('Kim')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()