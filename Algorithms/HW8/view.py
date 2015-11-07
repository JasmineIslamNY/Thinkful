from flask import Flask, render_template, request, redirect, url_for
from main import Main


app = Flask(__name__)
main = Main()

@app.route("/", methods=['GET'])
def displaySolution():
	display_problem = main.display_problem
	interim = main.interim
	solution = main.solution

	return render_template('shunting.html', display_problem=display_problem, interim=interim, solution=solution, title='Shunting-Yard Algorithm')
	

@app.route("/", methods=['POST'])
def problemInput():

	input=request.form["problem"]
	main.calculate(input)
	
	return redirect(url_for("displaySolution"))
	
if __name__ == "__main__":
	app.run(debug=True)

