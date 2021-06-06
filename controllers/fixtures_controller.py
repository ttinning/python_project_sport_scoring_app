import pdb
from flask import Flask, render_template, request, redirect, Blueprint

fixtures_blueprint = Blueprint("fixtures", __name__)

import repositories.fixture_repository as fixture_repository
import repositories.team_repository as team_repository

from models.fixture import Fixture

@fixtures_blueprint.route("/fixtures")
def fixtures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()
    return render_template("fixtures/index.html", fixtures-fixtures, teams=teams)

@fixtures_blueprint.route("/fixtures/new", methods=["GET"])
def new_fixture():
    teams = team_repository.select_all()
    return render_template("fixtures/new.html", teams=teams)

@fixtures_blueprint.route("/fixtures", methods=["POST"])
def create_fixture():
    team_1 = request.form["team_1"]
    team_1_score = request.form["team_1_score"]
    team_2 = request.form["team_2"]
    team_2_score = request.form["team_2_score"]
    fixture = Fixture(team_1, team_1_score,  team_2, team_2_score, id)
    fixture_repository.save(fixture)
    return redirect("/fixtures")

@fixtures_blueprint.route("/fixtures/<id>")
def show_fixture(id):
    fixture = fixture_repository.select(id)
    return render_template("/fixtures/index.html")

@fixtures_blueprint.route("/fixtures/<id>/edit")
def edit_team(id):
    fixture = fixture_repository.select(id)
    team = team_repository.select_all()
    return render_template("fixtures/edit.html")

@fixtures_blueprint.route("/fixtures/<id>", methods=["POST"])
def update_team(id):
    team_1 = request.form["team_1"]
    team_1_score = request.form["team_1_score"]
    team_2 = request.form["team_2"]
    team_2_score = request.form["team_2_score"]
    fixture = Fixture(team_1, team_1_score, team_2, team_2_score, id)
    fixture_repository.update(fixture)
    return redirect("/fixtures")

@fixtures_blueprint.route("/fixtures/<id>/delete", methods=["POST"])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect ("/fixtures")