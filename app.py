from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

##### Code here ######
@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/reviews')
def reviews():
	return render_template("reviews.html")

@app.route('/outfits')
def outfits():
	return render_template("outfits.html")	
#####################


if __name__ == '__main__':
    app.run(debug=True)