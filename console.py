import pdb

from models.team import Team
import repositories.team_repository as team_repository

# from models.fixture import Fixture
# import repositories.fixture_repository as fixture_repository


team_repository.delete_all()
# fixture_repository.delete_all()

team_1 = Team("Eagles", "Philadelphia")
team_repository.save(team_1)

team_2 = Team("Cowboys", "Dallas")
team_repository.save(team_2)

team_3 = Team("Seahawks", "Seattle")
team_repository.save(team_3)

team_4 = Team("Steelers", "Pittsburgh")
team_repository.save(team_4)

# fixture_1 = Fixture(team_1, 15, team_2, 5)
# fixture_repository.save(fixture_1)

# fixture_2 = Fixture(team_3, 23, team_4, 32)
# fixture_repository.save(fixture_2)

# fixture_3 = Fixture(team_4, 0, team_1, 0)
# fixture_repository.save(fixture_3)

# fixture_4 = Fixture(team_2, 0, team_3, 0)
# fixture_repository.save(fixture_4)


pdb.set_trace()

