import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen, f'Тест test_walk пропущен: Тесты в этом кейсе заморожены')
    def test_walk(self):
        first = Runner('Petr')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    @unittest.skipIf(is_frozen, f'Тест test_run пропущен: Тесты в этом кейсе заморожены')
    def test_run(self):
        second = Runner("Fedor")
        for i in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

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

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, f'Тест setUp пропущен: Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run1 = Runner('Усейн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for race, participants in cls.all_results.items():
            print(" и ".join(participants))

    @unittest.skipIf(is_frozen, f'Тест test_race1 пропущен: Тесты в этом кейсе заморожены')
    def test_race1(self):
        # Участвуют Усэйн и Ник
        tournament = Tournament(90, self.run1, self.run3)
        results = tournament.start()
        cls_result = [runner.name for runner in results.values()]  # Собираем имена участников
        self.all_results["Усэйн и Ник"] = cls_result  # Сохраняем их в all_results

        # Проверяем, что Ник всегда последний
        last_runner = list(results.values())[-1]
        self.assertTrue(last_runner.name == "Ник")

    @unittest.skipIf(is_frozen, f'Тест test_race2 пропущен: Тесты в этом кейсе заморожены')
    def test_race2(self):
        # Участвуют Андрей и Ник
        tournament = Tournament(90, self.run2, self.run3)
        results = tournament.start()
        cls_result = [runner.name for runner in results.values()]  # Собираем имена участников
        self.all_results["Андрей и Ник"] = cls_result  # Сохраняем их в all_results

        # Проверяем, что Ник всегда последний
        last_runner = list(results.values())[-1]
        self.assertTrue(last_runner.name == "Ник")

    @unittest.skipIf(is_frozen, f'Тест test_race3 пропущен: Тесты в этом кейсе заморожены')
    def test_race3(self):
        # Участвуют Усэйн, Андрей и Ник
        tournament = Tournament(90, self.run1, self.run2, self.run3)
        results = tournament.start()
        cls_result = [runner.name for runner in results.values()]  # Собираем имена участников
        self.all_results["Усэйн, Андрей и Ник"] = cls_result  # Сохраняем их в all_results

        # Проверяем, что Ник всегда последний
        last_runner = list(results.values())[-1]
        self.assertTrue(last_runner.name == "Ник")