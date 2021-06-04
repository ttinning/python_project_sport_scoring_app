class Fixture:

    def __init__(self, away_team, away_score, home_team, home_score, id=None):
        self.away_team = away_team
        self.away_score = away_score
        self.home_team = home_team
        self.home_score = home_score
        self.id = id

    def result(self):
        if self.away_score == self.home_score:
            return None
        elif self.away_score > self.home_score:
            return self.away_team
        elif self.away_score < self.home_score:
            return self.home_team
