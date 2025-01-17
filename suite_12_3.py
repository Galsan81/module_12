import unittest

import test_12_3


nocalcST = unittest.TestSuite()

nocalcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
nocalcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(nocalcST)