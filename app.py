from flask import Flask, render_template, redirect, session, request, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "NAFQJQL"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home_page():
    return render_template('home.html', title="Home")

@app.route('/start')
def start():
    #This route's purpose is to initialize a session that persists through a user's use time.
    #A board, words entered, and a point system will be shown for the user to see their progress. 
    #A timer will be added when the final product is done. 
    
    new_board = boggle_game.make_board()
    session["board"] = new_board
    session["words"] = ["foo", "bar", "hello", "world"]
    session["points"] = 0

    return redirect('/game-on')

@app.route('/game-on')
def game_on():
    #This route's purpose is to create the viewable board, along with a point system, a record of valid words used, and time.
    #Take note that sessions are cookie based, and will persist throughout the same browser. Meaning, opening a new tab and playing the game will result in the same board. 
    #but the opposite is true for when the user uses a different browser. This means that the boards generated will be unique to each unique device. 
    board = session["board"]
    total = session.get('points')

    return render_template('game.html', title="Game", total=total, board=board)

@app.route('/check-answer', methods=["POST"])
def check_data():
    user_input = []
    json_data = jsonify(list(user_input))

    if boggle_game.check_valid_word(session["board"], json_data):
        new_words = session["words"].append(json_data)
        session["words"] = new_words


    return json_data
# @app.route('/check-answer')
# def validating():
#     """Check if the word is in dictionary, and is present in the board."""

#     word = request.args["answer"]
#     board = session["board"]
#     isValid = boggle_game.check_valid_word(board, word)
#     return 