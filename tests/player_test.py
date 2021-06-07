import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Justin Fields", 1, "QB", 1, 1500, 600)

    def test_player_has_name(self):
        expected = "Justin Fields"
        actual = self.player_1.player_name
        self.assertEqual(expected, actual)

    def test_player_has_team_id(self):
        expected = 1
        actual = self.player_1.team_id
        self.assertEqual(expected, actual)

    def test_player_has_position(self):
        expected = "QB"
        actual = self.player_1.position
        self.assertEqual(expected, actual)

    def test_player_has_number(self):
        expected = 1
        actual = self.player_1.jersey_number
        self.assertEqual(expected, actual)

    def test_player_has_passing_yards(self):
        expected = 1500
        actual = self.player_1.passing_yards
        self.assertEqual(expected, actual)

    def test_player_has_rushing_yards(self):
        expected = 600
        actual = self.player_1.rushing_yards
        self.assertEqual(expected, actual)