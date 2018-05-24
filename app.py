# import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
#from flask_pymongo import PyMongo

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#mongo = PyMongo(app)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.surf_db

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
    #Get surf_db
    surfdata=db.surfsummary.find()
    

    return render_template("index.html", list=surfdata)

    # Redirect back to home page
    #return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
