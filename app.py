from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route('/')
def index():
    logging.info("Rendering Template")
    return render_template('mobile.html')

app.run(debug=True)