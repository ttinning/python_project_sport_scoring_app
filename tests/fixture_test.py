import unittest
from models.team import Team
from models.fixture import Fixture

class TestFixture(unittest.TestCase):

    def setUp(self):
        self.team_1 = Team("Saints", "New Orleans")
        self.team_2 = Team("Rams", "Los Angeles")
        self.team_3 = Team("Bears", "Chicago")
        self.fixture_1 = Fixture(self.team_1.name, 21, self.team_2.name, 15)
        self.fixture_2 = Fixture(self.team_3.name, 5, self.team_2.name, 21)
        self.fixture_3 = Fixture(self.team_1.name, 21, self.team_2.name, 21)

    def test_fixture_1_has_away_team_name(self):
        expected = "Saints"
        actual = self.fixture_1.away_team
        self.assertEqual(expected, actual)

    def test_fixture_2_has_home_team_name(self):
        expected = "Rams"
        actual = self.fixture_1.home_team
        self.assertEqual(expected, actual)

    def test_fixture_1_has_away_team_score(self):
        expected = 21
        actual = self.fixture_1.away_score
        self.assertEqual(expected, actual)
    
    def test_fixture_2_has_home_team_score(self):
        expected = 21
        actual = self.fixture_2.home_score
        self.assertEqual(expected, actual)

    def test_winner_of_fixture_1__away_team(self):
        expected = "Saints"
        actual = self.fixture_1.result()
        self.assertEqual(expected, actual)

    def test_winner_of_fixture_2__home_team(self):
        expected = "Rams"
        actual = self.fixture_2.result()
        self.assertEqual(expected, actual)

    def test_winner_of_fixture_3__returns_none(self):
        expected = None
        actual = self.fixture_3.result()
        self.assertEqual(expected, actual)
