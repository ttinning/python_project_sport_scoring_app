class Fixture:

    def __init__(self, team_1, team_1_score, team_2, team_2_score, id=None):
        self.team_1 = team_1
        self.team_1_score = team_1_score
        self.team_2 = team_2
        self.team_2_score = team_2_score
        self.id = id

    def result(self):
        if self.team_1_score == self.team_2_score:
            return None
        elif self.team_1_score > self.team_2_score:
            return self.team_1
        elif self.team_1_score < self.team_2_score:
            return self.team_2
