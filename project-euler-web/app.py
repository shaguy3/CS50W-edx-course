from flask import Flask, render_template, request
from lowest_divisible import smallest_divisible

app = Flask(__name__)

@app.route('/')
def no_answer():
	answer = ''
	return (render_template('index.html', answer=answer))

@app.route('/lowest-divisible', methods=['POST'])
def lowest_divisible():
	top_number = request.form.get('top_number')
	if top_number == '':
		return (render_template('index.html', answer='please enter a number'))
	else:
		answer = smallest_divisible(int(top_number))
		return (render_template('index.html', answer=answer))
	#f'The smallest number that is divisible by all of the numbers, 1 to {top_number}, is {sd}