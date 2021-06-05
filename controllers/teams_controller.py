from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

#INDEX
@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("/teams/index.html", teams=teams)

#NEW
@teams_blueprint.route("/teams/new")
def new_team():
    teams = team_repository.select_all()
    return render_template("teams/new.html", teams=teams)

#CREATE
#POST METHOD
@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["team_name"],
    location = request.form["location"]
    new_team = Team(name, location)
    team_repository.save(new_team)
    return redirect("/teams")
    
# EDIT
@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template("teams/edit.html", team=team)

# UPDATE
# POST METHOD
@teams_blueprint.route("/teams/<id>", methods=["POST"])
def update_team(id):
    name = request.form["team_name"]
    location = request.form["location"]
    team = Team(name, location, id)
    team_repository.update(team)
    return redirect("/teams")

# DELETE
# POST METHOD
@teams_blueprint.route("/teams/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/teams")
