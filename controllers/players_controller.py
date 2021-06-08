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
    return render_template("teams/players/new.html", teams=teams)

@players_blueprint.route("/teams/players", methods=["POST"])
def create_player():
    player_name = request.form["player_name"]
    team_id = request.form["team_id"]
    position = request.form["position"]
    jersey_number = request.form["jersey_number"]
    passing_yards = request.form["passing_yards"]
    rushing_yards = request.form["rushing_yards"]
    team = team_repository.select(team_id)
    print(team_id)
    new_player = Player(player_name, team, position, jersey_number, passing_yards, rushing_yards)
    player_repository.save(new_player)
    return redirect("/teams/players")

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
    player_name = request.form["player_name"]
    team_id = request.form["team_id"]
    position = request.form["position"]
    jersey_number = request.form["jersey_number"]
    passing_yards = request.form["passing_yards"]
    rushing_yards = request.form["rushing_yards"]
    team_1 = team_repository.select(int(team_id))
    player = Player(player_name, team_1, position, jersey_number, passing_yards, rushing_yards, id)
    player_repository.update(player)
    return redirect("/teams/players")

@players_blueprint.route("/teams/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/teams/players")


