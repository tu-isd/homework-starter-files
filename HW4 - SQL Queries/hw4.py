from flask import Flask, render_template

import db

app = Flask(__name__)

@app.route('/trips')
def trip_report():
    render_template()

app.run(debug=True)
