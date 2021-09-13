from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/parser/api/article', methods = ['GET'])
def info():
	
	return 'Hello'


if __name__ == '__main__':
	app.run(debug=True)