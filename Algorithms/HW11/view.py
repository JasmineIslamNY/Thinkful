from flask import Flask, render_template, request, redirect, url_for
from main import Main


app = Flask(__name__)
main = Main()

@app.route("/", methods=['GET'])
def output():
	input = main.input
	list = main.list
	bitVectorDisplay = main.bitVectorDisplay 
	inclusionTest = main.inclusionTest

	return render_template('bloom.html', input=input, list=list, bitVectorDisplay=bitVectorDisplay, inclusionTest=inclusionTest) 
	

@app.route("/", methods=['POST'])
def input():

	input=request.form['input']
	main.processInput(input) 
	
	return redirect(url_for("output"))
	
if __name__ == "__main__":
	app.run(debug=True)

