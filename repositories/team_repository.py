from db.run_sql import run_sql
from models.team import Team
from models.fixture import Fixture
from models.player import Player

def save(team):
    sql = "INSERT INTO teams (name, location) VALUES (%s, %s) RETURNING id"
    values = [team.name, team.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["name"], result["location"], result["id"])
        teams.append(team)
    return teams

def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    team = Team(result["name"], result["location"], result["id"])
    return team

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET (name, location) = (%s, %s) WHERE id = %s"
    values = [team.name, team.location, team.id]
    run_sql(sql,values)

def show_fixtures(team):
    fixtures = []

    sql = "SELECT * FROM fixtures WHERE team_1_id = %s or team_2_id = %s"
    values = [team.id, team.id]
    results = run_sql(sql, values)

    for row in results:
        team_1 = select(row["team_1_id"])
        team_2 = select(row["team_2_id"])
        fixture = Fixture(team_1, row["team_1_score"], team_2, row["team_2_score"], row["id"])
        fixtures.append(fixture)

    return fixtures

def show_players(team):
    players = []

    sql = "SELECT * FROM players WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        team = select(row["team_id"])
        player = Player(row["player_name"], team, row["position"], row["jersey_number"], row["passing_yards"], row["rushing_yards"], row["id"])
        players.append(player)

    return players