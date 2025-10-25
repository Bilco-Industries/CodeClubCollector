# Flask documentation:
# https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, request, render_template
import sqlite3;

from logger import logger

app = Flask(__name__)
includeFooter = True

# based on code shown here:
# https://www.geeksforgeeks.org/python/how-to-serve-static-files-in-flask/
@app.route("/", methods=["get"])
def index():
    logger.debug('Serving index.html')
    return render_template('index.html', footer=includeFooter)

@app.route("/docs", methods=["get"])
def docs():
    return render_template('docs.html', footer=includeFooter)

# configure an endpoint to accept data from other devices
def post_data():
    return None

if __name__ == "__main__":
    app.run()