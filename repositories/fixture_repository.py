from db.run_sql import run_sql
from models.fixture import Fixture
from models.team import Team
import repositories.team_repository as team_repository

def save(fixture):
    sql = "INSERT INTO fixtures (team_1, team_1_score, team_2, team_2_score) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [fixture.team_1.id, fixture.team_1_score, fixture.team_2.id, fixture.team_2_score]
    results = run_sql(sql, values)
    fixture.id = results[0]['id']
    return fixture

def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for result in results:
        team_1 = team_repository.select(result["team_1"])
        team_2 = team_repository.select(result["team_2"])
        fixture = Fixture(team_1, result["team_1_score"], team_2, result["team_2_score"], result["id"])
        fixtures.append(fixture)
    return fixtures

def select(id):
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    fixture = Fixture(result["team_1"], result["team_1_score"], result["team_2"],result["team_2_score"], result["id"])
    return fixture

def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(fixture):
    sql = "UPDATE fixtures SET (team_1, team_1_score, team_2, team_2_score = (%s, %s, %s, %s) WHERE id = %s"
    values = [fixture.team_1, fixture.team_1_score, fixture.team_2, fixture.team_2_score, fixture.id]
    run_sql(sql, values)

    