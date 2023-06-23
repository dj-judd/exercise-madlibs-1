from flask import Flask, render_template, request, session
from random import choice

app = Flask(__name__)
app.secret_key = "secret-key" # replace with your own secret key

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

@app.route("/")
def landing_page():
    """Display homepage."""
    return render_template("index.html")

@app.route("/hello")
def say_hello():
    """Say hello to user."""
    return render_template("hello.html")

@app.route("/greet")
def greet_person():
    """Greet user with compliment."""
    session['player'] = request.args.get("player")  # Store player's name in session
    compliment = choice(AWESOMENESS)
    return render_template("compliment.html", player=session['player'], compliment=compliment)

@app.route("/game")
def show_madlib_form():
    wants_to_play_game = request.args.get("RadioSelection")
    if wants_to_play_game == "yes":
        return render_template("game.html", player=session['player'])  # Fetch player's name from session
    else:
        player_name = session.get('player')  # Get the player's name before removing it
        session.pop('player', None)  # Remove player from session
        return render_template("goodbye.html", player=player_name)

@app.route("/madlib")
def show_madlib(): 
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    return render_template("madlib.html",
                           color=color,
                           noun=noun,
                           name=session['player'],  # Fetch player's name from session
                           adjective=adjective)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
