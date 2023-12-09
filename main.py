from flask import flask, jsonify, requests, render_template
import smptlib


app = flask.Flask(__name__)

@app.route('/')
def home():
    return return_render('index.html')

@app.route('/payment', method=['GET', 'POST'])
def payment():
    return render_template('card.html')


if __name__ == '__main__':
    app.run(debug=True)
