

from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        first = Runner('Petr')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = Runner("Fedor")
        for i in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        first1 = Runner('Petr')
        sec2 = Runner('Fedor')
        for i in range(10):
            first1.walk()
        for i in range(10):
            sec2.run()
        self.assertNotEqual(first1.distance, sec2.distance)

if __name__=='__main__':
    unittest.main()