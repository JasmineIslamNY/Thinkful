from game import Game
from flask import Flask, render_template


app = Flask(__name__)
game = Game()


@app.route("/")
def gameBoard():	
	tower1 = game.tower1.peek()
	tower2 = game.tower2.peek()
	tower3 = game.tower3.peek()
	return render_template('game.html', tower1 = tower1, tower2 = tower2, tower3 = tower3, title='Towers of Hanoi')


if __name__ == "__main__":
	app.run(debug=True)

