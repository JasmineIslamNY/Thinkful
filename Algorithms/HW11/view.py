from flask import Flask, render_template, request, redirect, url_for
from main import Main


app = Flask(__name__)
main = Main()

@app.route("/", methods=['GET'])
def output():
	input = main.input
	output = main.output

	return render_template('convert.html', input=input, output=output) 
	

@app.route("/", methods=['POST'])
def input():

	input=request.form['input']
	main.processInput(input) 
	
	return redirect(url_for("output"))
	
if __name__ == "__main__":
	app.run(debug=True)

