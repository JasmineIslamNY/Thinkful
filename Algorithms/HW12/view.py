from flask import Flask, render_template, request, redirect, url_for
from main import Main


app = Flask(__name__)
main = Main()

@app.route("/", methods=['GET'])
def output():
	input = main.input
	output = main.output
	label =	main.label

	return render_template('compress_view.html', input=input, output=output, label=label) 
	

@app.route("/", methods=['POST'])
def input():

	if request.form['submit'] == 'encode':
		input=request.form['input']
		main.encodeInput(input) 
	elif request.form['submit'] == 'decode':
		input=request.form['input']
		main.decodeInput(input) 

	return redirect(url_for("output"))
	
if __name__ == "__main__":
	app.run(debug=True)

