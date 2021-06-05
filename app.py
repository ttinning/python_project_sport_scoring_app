from flask import Flask, render_template
from controllers.teams_controller import teams_blueprint

app = Flask(__name__)

app.register_blueprint(teams_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__name__':
    app.run()