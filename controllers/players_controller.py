from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route("/teams/players")
def players():
    players = player_repository.select_all()
    teams = team_repository.select_all()
    return render_template("teams/players/index.html", players=players, teams=teams)

@players_blueprint.route("/teams/players/new")
def new_player():
    teams = team_repository.select_all()
    return render_template("clubs/players/new.html")

@players_blueprint.route("/teams/players/<id>")
def show_player(id):
    player = player_repository.select(id)
    teams = team_repository.select_all()
    return render_template("teams/players/show.html", player=player, teams=teams)

@players_blueprint.route("/teams/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    teams = team_repository.select_all()
    return render_template("teams/players/edit.html", player=player, teams=teams)

@players_blueprint.route("/teams/players/<id>", methods=["POST"])
def update_player(id):
    name = request.form["player_name"]
    team_id = request.form["team_id"]
    position = request.form["position"]
    number = request.form["number"]
    passing_yards = request.form["passing_yards"]
    rushing_yards = request.form["rushing_yards"]
    player = Player(name, team_id, position, number, passing_yards, rushing_yards)
    player_repository.update(player)
    return redirect("/teams/players")

@players_blueprint.route("/teams/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/teams/players")


