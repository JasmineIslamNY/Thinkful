from flask import Flask, render_template, request, redirect, url_for
from shunting import Shunting
from reversepolishnotation import ReversePolishNotation


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def problemInput():
	input=request.form["problem"]

	Dijkstra = Shunting(input)
	interim = Dijkstra.outputQueue.peek()

	Polish = ReversePolishNotation(Dijkstra.outputQueue)
	solution = Polish.outputStack.peek()

	return render_template('shunting.html', display_problem=input, interim=interim, solution=solution, title='Shunting-Yard Algorithm')
	
if __name__ == "__main__":
	app.run(debug=True)

