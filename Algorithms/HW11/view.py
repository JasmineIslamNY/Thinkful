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

	if request.form['submit'] == 'word':
		input=request.form['input']
		main.processInput(input) 
	elif request.form['submit'] == 'checkWord':
		check=request.form['check']
		main.testInclusion(check) 
	elif request.form['submit'] == 'random':
		random=request.form['random']
		main.loadRandomWord(random) 
	
	return redirect(url_for("output"))
	
if __name__ == "__main__":
	app.run(debug=True)

