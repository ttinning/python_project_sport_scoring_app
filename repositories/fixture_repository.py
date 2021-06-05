from db.run_sql import run_sql
from models.fixture import Fixture
from models.team import Team
import repositories.team_repository as team_repository

def save(fixture):
    sql = "INSERT INTO fixtures (team_1_id, team_2_id) VALUES (%s, %s) RETURNING id"
    values = [fixture.team_1, fixture.team_2]
    reuslts = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id

def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for result in results:
        team_1 = team_repository.select(result["team_1_id"])
        team_2 = team_repository.select(result["team_2_id"])
        fixture = Fixture(team_1, team_2, result["id"])
        fixtures.append(fixture)
    return fixtures

def select(id):
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    fixture = Fixture(result["team_1_id"], result["team_2_id"], result["id"])
    return fixture

def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)