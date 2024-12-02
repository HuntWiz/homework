import unittest
from pprint import pprint

import exm_for_tests


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = exm_for_tests.Runner('Усейн',10)
        self.runner2 = exm_for_tests.Runner('Андрей', 9)
        self.runner3 = exm_for_tests.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament(self):
        tour = exm_for_tests.Tournament(90, self.runner1, self.runner2, self.runner3)
        tourpls = tour.start()
        self.all_results.append(tourpls)

        self.assertTrue(tourpls[3] == self.runner3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tour = exm_for_tests.Tournament(90, self.runner1, self.runner3)
        tourpls = tour.start()
        self.all_results.append(tourpls)

        self.assertTrue(tourpls[2] == self.runner3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tour = exm_for_tests.Tournament(90, self.runner2, self.runner3)
        tourpls = tour.start()
        self.all_results.append(tourpls)

        self.assertTrue(tourpls[2] == self.runner3.name)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = exm_for_tests.Runner('Jim')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = exm_for_tests.Runner('Jim')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = exm_for_tests.Runner('Jim')
        runner2 = exm_for_tests.Runner('Kim')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()