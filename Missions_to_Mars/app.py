from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    missions = mongo.db.missions.find_one()
    return render_template("index.html", missions=missions)


@app.route("/scrape")
def scraper():
    missions = mongo.db.missions
    missions_data = scrape_mars.scrape()
    missions.update({}, missions_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
