import random
import flask
from User_Agent import User_Agent

app = flask.Flask(__name__)


@app.route('/')
def index():
	return flask.render_template('op.html')


@app.route('/i')
def i():
	return flask.render_template('op.html')


if __name__ == '__main__':
	app.run(host='192.168.4.92', port=4000)
