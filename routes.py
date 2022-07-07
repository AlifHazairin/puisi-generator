from flask import Blueprint, render_template, redirect, request

generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
	return render_template('index.html')

@generator.route('/analyze', method=["POST"])
def analyze():
	title = request.form['title']
	text = ai.generate_text(title)
	return render_template('index.html', text=text)