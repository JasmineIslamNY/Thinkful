from flask import Flask, render_template, request, redirect, url_for
from main import Main


app = Flask(__name__)
main = Main()

@app.route("/", methods=['GET'])
def output():
	input = main.input
	dokOutput = str(main.dokOutput)
	lolOutput = str(main.lolOutput)
	yaleOutput = str(main.yaleOutput)

	return render_template('convert.html', input=input, dokOutput=dokOutput, lolOutput=lolOutput, yaleOutput=yaleOutput) 
	

@app.route("/", methods=['POST'])
def input():

	input=request.form['input']
	main.processInput(input) 
	
	return redirect(url_for("output"))
	
if __name__ == "__main__":
	app.run(debug=True)

