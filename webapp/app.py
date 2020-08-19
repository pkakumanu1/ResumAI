from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)


# Route to render index.html 
@app.route("/")
def home():

    # Return template and data
    return render_template("index.html")


# Route that will trigger the scrape function
@app.route("/about")
def about():

    return render_template("about.html")


if __name__ == "__main__":
    app.run()
