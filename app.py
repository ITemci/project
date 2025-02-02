# import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import login_required
import random


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# HOME
@app.route("/")
@login_required
def index():



    return render_template("index.html")


    #return render_template("index.html", stocks=stocks,balance=balance[0]["cash"],quote=quote["price"])




# LOG IN
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()


    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)





        # Remember which user has logged in
        session["user_id"] = random.randint(1000, 9999)
        session["user_name"] = request.form.get("username")

           # Query database for username uniqueness
        rows = db.execute( "SELECT * FROM users where user_id = ?", session["user_id"] )
        if len(rows)==1:
            session["user_id"] = random.randint(1000, 9999)

        # saving user info in database
        db.execute("insert into users values(?,?)",session["user_id"], session["user_name"])


        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# LOG OUT
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/submit",methods=["POST"])
@login_required
def submit():
    selected_options = {}

    # Get the selected values from the form data
    for i in range(1, 7):  # Assuming you have 6 questions
        question_name = f'option_div{i}'
        selected_option = request.form.get(question_name)
        selected_options[f'q{i}'] = selected_option


    db.execute("insert into results(user_id,q1,q2,q3,q4,q5,q6) values(?,?,?,?,?,?,?)", session["user_id"],selected_options['q1'], selected_options['q2'], selected_options['q3'], selected_options['q4'], selected_options['q5'], selected_options['q6'])

    # getting results from DB (latest entry) of logged in user
    # results = db.execute("select q1,q2,q3,q4,q5,q6 from results where user_id = ? ORDER BY time_stamp DESC LIMIT 1",session["user_id"])





    return render_template("results.html",results=selected_options)

    # generate a chart with all questions and answers from db, of all users with pandas or ...
