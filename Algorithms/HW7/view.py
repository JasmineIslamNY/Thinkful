from game import Game
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
game = Game()


@app.route("/", methods=['GET'])
def gameBoard():	
	tower1 = game.tower1.peek()
	tower2 = game.tower2.peek()
	tower3 = game.tower3.peek()
	moves = game.moves
	from_tower = game.displayFromTower()
	return render_template('game.html', tower1 = tower1, tower2 = tower2, tower3 = tower3, moves=moves, from_tower=from_tower, title='Towers of Hanoi')


@app.route("/", methods=['POST'])
def moveDisk():
	if request.form['submit'] == 'tower1':
		button = 'tower1'
		game.buttonPressed(button)
	elif request.form['submit'] == 'tower2':
		button = 'tower2'
		game.buttonPressed(button)
	elif request.form['submit'] == 'tower3':
		button = 'tower3'
		game.buttonPressed(button)
	elif request.form['submit'] == 'reset':
		button = 'reset'
		game.buttonPressed(button)

	return redirect(url_for("gameBoard"))
	
if __name__ == "__main__":
	app.run(debug=True)

