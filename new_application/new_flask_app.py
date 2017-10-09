from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/word')
def word():
	return render_template('characters.html')

@app.route('/results', methods = ['GET', 'POST'])
def count():
	if request.method == 'GET':
		result = request.args
		sentence = str(result['yourCharacters'])
		number = len(sentence)
		return "Your word/sentence has " + str(number) + " characters in it!"

@app.route('/vowels')
def word2():
	return render_template('vowels.html')

@app.route('/results2', methods = ['GET', 'POST'])
def countVowels():
	if request.method == 'GET':
		result2 = request.args
		sentence2 = str(result2['yourVowels'])
		count = 0
		vowelsSet = set("aeiou")
		for letter in sentence2:
		    if letter in vowelsSet:
		        count += 1
		return "Your word/sentence has " + str(count) + " vowels in it"


if __name__ == '__main__':
	app.run()