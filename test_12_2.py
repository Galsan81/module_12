import unittest
from runner_and_tournament import Runner, Tournament
import pprint

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.run1 = Runner('Усейн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for race, participants in cls.all_results.items():
            print(" и ".join(participants))

    def test_race1(self):
        # Участвуют Усэйн и Ник
        tournament = Tournament(90, self.run1, self.run3)
        results = tournament.start()
        cls_result = [runner.name for runner in results.values()]  # Собираем имена участников
        self.all_results["Усэйн и Ник"] = cls_result  # Сохраняем их в all_results

        # Проверяем, что Ник всегда последний
        last_runner = list(results.values())[-1]
        self.assertTrue(last_runner.name == "Ник")

    def test_race2(self):
        # Участвуют Андрей и Ник
        tournament = Tournament(90, self.run2, self.run3)
        results = tournament.start()
        cls_result = [runner.name for runner in results.values()]  # Собираем имена участников
        self.all_results["Андрей и Ник"] = cls_result  # Сохраняем их в all_results

        # Проверяем, что Ник всегда последний
        last_runner = list(results.values())[-1]
        self.assertTrue(last_runner.name == "Ник")

    def test_race3(self):
        # Участвуют Усэйн, Андрей и Ник
        tournament = Tournament(90, self.run1, self.run2, self.run3)
        results = tournament.start()
        cls_result = [runner.name for runner in results.values()]  # Собираем имена участников
        self.all_results["Усэйн, Андрей и Ник"] = cls_result  # Сохраняем их в all_results

        # Проверяем, что Ник всегда последний
        last_runner = list(results.values())[-1]
        self.assertTrue(last_runner.name == "Ник")