class Player:

    def __init__(self, player_name, team_id, position, jersey_number, passing_yards, rushing_yards, id=None):
        self.player_name = player_name
        self.team_id = team_id
        self.position = position
        self.jersey_number = jersey_number
        self.passing_yards = passing_yards
        self.rushing_yards = rushing_yards
        self.id = id