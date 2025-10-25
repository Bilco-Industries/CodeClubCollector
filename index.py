# Flask documentation:
# https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask, request, render_template;
from database import database
from logger import logger

app = Flask(__name__)
db: database.DB = database.DB()

# based on code shown here:
# https://www.geeksforgeeks.org/python/how-to-serve-static-files-in-flask/
@app.route("/", methods=["get"])
def index():
    records = None
    try:
        user = request.args.get('name')
        if user:
            records = db.get_data_for_user(user)
    except:
        pass
    logger.debug(records)
    return render_template('index.html', records=records)
    

@app.route("/docs", methods=["get"])
def docs():
    return render_template('docs.html')

# configure an endpoint to accept data from other devices
@app.route("/<name>", methods=["post"])
def recieve_data(name):
    try:
        content = request.get_json()
        logger.debug(f"Recieved {name} {content}")

        db.write_data_for_user(
            user=name,
            lux=content['lux'],
            pressure=content['pressure_hpa'],
            temp=content['temp_c'],
            humidity=content['humidity_pct'],
        )

        return "Success"

    except Exception as e:
        logger.error(e)
        raise e



if __name__ == "__main__":
    app.run()