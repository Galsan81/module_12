import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(levelname)s | %(message)s | %(asctime)s')
class RunnerTest(unittest.TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen, f'Тест test_walk пропущен: Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            first = Runner('Petr', -5)
            for i in range(10):
                first.walk()
            self.assertEqual(first.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, f'Тест test_run пропущен: Тесты в этом кейсе заморожены')
    def test_run(self):
        try:

            second = Runner(78)
            for i in range(10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as te:
            logging.warning('Неверный тип данных для объекта Runner')
    @unittest.skipIf(is_frozen, f'Тест test_challtnge пропущен: Тесты в этом кейсе заморожены')
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
