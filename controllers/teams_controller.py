from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.teams_repository as team_repository

teams_repository = Blueprint("teams", __name__)

#INDEX
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("/teams/index.html", teams=teams)

#NEW


#CREATE
#POST METHOD


# EDIT


# UPDATE
# POST METHOD


# DELETE
# POST METHOD
