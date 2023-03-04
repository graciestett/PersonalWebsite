from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/about")
def about_me():
    return render_template("about_me.html")
    
def todays_date():
    today = date.today()
    str_date = today.strftime("%B %d %Y")
    return "Today's date is " + str_date
    

