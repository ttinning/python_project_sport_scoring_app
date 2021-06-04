from db.run_sql import run_sql
from models.fixture import Fixture
from models.team import Team
import repositories.team_repository as team_repository

def save(fixture):
    sql = "INSERT INTO fixtures (away_team_id, home_team_id) VALUES (%s, %s) RETURNING id"
    values = [fixture.away_team, fixture.home_team]
    reuslts = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id

def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for result in results:
        away_team = team_repository.select(result["away_team_id"])
        home_team = team_repository.select(result["home_team_id"])
        fixture = Fixture(away_team, home_team, result["id"])
        fixtures.append(fixture)
    return fixtures

def select(id):
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    fixture = Fixture(result["away_team_id"], result["home_team_id"], result["id"])
    return fixture

def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)