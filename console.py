import pdb

from models.team import Team
import repositories.team_repository as team_repository

from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository


team_repository.delete_all()
fixture_repository