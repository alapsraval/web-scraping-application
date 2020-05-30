from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask class
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# route() decorator to tell Flask what URL should trigger index() function.
# The function name is also used to generate URLs for that particular function, and return the content in the browser.
# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    missions = mongo.db.missions.find_one()
    # Return template and data
    return render_template("index.html", missions=missions)

# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():
    # Run the scrape function
    missions_data = scrape_mars.scrape()
    # Update the Mongo database using update and upsert=True
    missions = mongo.db.missions
    missions.update({}, missions_data, upsert=True)
    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

    # run "flask run" command to run the app