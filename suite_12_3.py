import unittest
import tests_12_3


suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

text = unittest.TextTestRunner(verbosity=2)
text.run(suite)

