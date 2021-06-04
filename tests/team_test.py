import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("Eagles", "Philadelphia")
        self.team2 = Team("Cowboys", "Dallas")

    def test_team1_has_team_name(self):
        expected = "Eagles"
        actual = self.team1.name
        self.assertEqual(expected, actual)

    def test_team2_has_team_name(self):
        expected = "Cowboys"
        actual = self.team2.name
        self.assertEqual(expected, actual)

    def test_team1_has_team_location(self):
        expected = "Philadelphia"
        actual = self.team1.location
        self.assertEqual(expected, actual)


    def test_team2_has_team_location(self):
        expected = "Dallas"
        actual = self.team2.location
        self.assertEqual(expected, actual)

    
