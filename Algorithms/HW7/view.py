from game import Game
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
game = Game()


@app.route("/", methods=['GET'])
def gameBoard():	
	tower1 = game.tower1.peek()
	tower2 = game.tower2.peek()
	tower3 = game.tower3.peek()
	return render_template('game.html', tower1 = tower1, tower2 = tower2, tower3 = tower3, title='Towers of Hanoi')


@app.route("/", methods=['POST'])
def moveDisk():
	if request.form['submit'] == 'tower1':
		tower = game.tower1
		print("Selected tower 1")
	elif request.form['submit'] == 'tower2':
		tower = game.tower2
		print("Selected tower 2")
	elif request.form['submit'] == 'tower3':
		tower = game.tower3
		print("Selected tower 3")

	if game.fromTower == None:
		game.fromTower = tower
		print("updated fromTower")
		return redirect(url_for("gameBoard"))
	else:
		game.toTower = tower
		game.moveDisk(game.fromTower, game.toTower)
		game.toTower = None
		game.fromTower = None
		print("Moved disk")
		return redirect(url_for("gameBoard"))

if __name__ == "__main__":
	app.run(debug=True)

