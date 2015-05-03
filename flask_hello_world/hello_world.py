import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_default():
        return "Hello World Default Page - add /hello or /hello/[YOUR_NAME] for other pages!"

@app.route("/hello")
def hello_world():
	return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
	html = """
		<h1>
			Hello {}!
		</h1>
		<p>
			Here's a picture of a lamb.  Awww...
		</p>
		<img src="http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2014/4/11/1397210130748/Spring-Lamb.-Image-shot-2-011.jpg">
	"""
        return html.format(name.title())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)

