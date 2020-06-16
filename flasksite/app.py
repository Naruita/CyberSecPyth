from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome/<username>')
def index(username):
	return render_template('hello.html', name=username)

@app.route('/success/<name>')
def success(name):
	return 'welcome %s' %name

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		username = request.form['nm']
		return redirect(url_for('success', name=username))
	else:
		username = request.args.get('nm')
		return redirect(url_for('success', name=username))

if __name__ == '__main__':
	app.run()
