
####### libs ##############################################

from flask import Flask, render_template, request, make_response, redirect, send_file, Response
from flask import jsonify, url_for

app = Flask(__name__)

@app.route("/")
def MainHandler():
	return render_template('index.html')


@app.route("/index")
def MainIHandler():
	return render_template('index.html')

@app.route("/service")
def MainSHandler():
	return render_template('services.html')

@app.route("/about")
def MainAHandler():
	return render_template('about.html')

@app.route("/contact")
def MainCHandler():
	return render_template('contact.html')

###### main #####

if __name__=="__main__":

	app.run(debug=True, host="0.0.0.0", port=80)
	# app.run(debug=True, host="0.0.0.0", port=6060)






