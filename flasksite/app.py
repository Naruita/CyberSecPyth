from flask import Flask

app = Flask(__name__)

@app.route('/profile/<float:id>')
def profile(id):
	return 'This profile belongs to %d' %id

if __name__ == '__main__':
	app.run()
