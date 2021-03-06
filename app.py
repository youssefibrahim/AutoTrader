from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup')
def signUp():
	return render_template('signup.html')

@app.route('/search')
def search():
	return render_template('search.html')

@app.route('/result', methods=["POST"])
def display_search():
	return render_template('result.html')

@app.route('/login')
def logIn():
	return render_template('login.html')

@app.route('/result')
def display_result():
	return render_template('result.html')
 
if __name__ == '__main__':
	app.run()