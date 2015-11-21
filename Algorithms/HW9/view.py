from flask import Flask, render_template, request, redirect, url_for
from main import Main


app = Flask(__name__)
main = Main()

@app.route("/", methods=['GET'])
def output():
	types = ['Convert', 'JSON to XML', 'XML to JSON']
	output = main.output
	input = main.input

	return render_template('convert.html', types=types, input=input, output=output)
	

@app.route("/", methods=['POST'])
def input():

	input=request.form['input']
	inputType=request.form['types']
	main.processInput(input, inputType)
	
	return redirect(url_for("output"))
	
if __name__ == "__main__":
	app.run(debug=True)

