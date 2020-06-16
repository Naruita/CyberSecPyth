from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello world'

@app.route('/new')
def new():
	return 'new page'

@app.route('/demo')
def demo():
	return 'this is the demo'

if __name__ == '__main__':
	app.run()
