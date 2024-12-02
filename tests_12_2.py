import unittest
from pprint import pprint

import exm_for_tests


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []


    def setUp(self):
        self.runner1 = exm_for_tests.Runner('Усейн',10)
        self.runner2 = exm_for_tests.Runner('Андрей', 9)
        self.runner3 = exm_for_tests.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(i)

    def test_tournament(self):
        tour = exm_for_tests.Tournament(90, self.runner1, self.runner2, self.runner3)
        tourpls = tour.start()
        self.all_results.append(tourpls)

        self.assertTrue(tourpls[3] == self.runner3.name)

    def test_tournament2(self):
        tour = exm_for_tests.Tournament(90, self.runner1, self.runner3)
        tourpls = tour.start()
        self.all_results.append(tourpls)

        self.assertTrue(tourpls[2] == self.runner3.name)

    def test_tournament3(self):
        tour = exm_for_tests.Tournament(90, self.runner2, self.runner3)
        tourpls = tour.start()
        self.all_results.append(tourpls)

        self.assertTrue(tourpls[2] == self.runner3.name)


if __name__ == '__main__':
    unittest.main()