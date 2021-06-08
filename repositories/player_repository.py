from db.run_sql import run_sql
from models.player import Player

def save(player):
    sql = "INSERT INTO players (player_name, team_id, position, jersey_number, passing_yards, rushing_yards) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [player.player_name, player.team_id, player.position, player.jersey_number, player.passing_yards, player. rushing_yards]
    results = run_sql(sql, values)
    print(results)
    id = results[0]["id"]
    player.id = id

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result["player_name"], result["team_id"], result["position"], result["jersey_number"], result["passing_yards"], result["rushing_yards"], result["id"])
        players.append(player)
    return players

def select(id):
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    player = Player(result["player_name"], result["team_id"], result["position"], result["jersey_number"], result["passing_yards"], result["rushing_yards"], result["id"])
    return player

def update(player):
    sql = "UPDATE players SET (player_name, team_id, position, jersey_number, passing_yards, rushing_yards) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [player.player_name, player.team.id, player.position, player.jersey_number, player.passing_yards, player.rushing_yards]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)