from flask import Flask, render_template, request, redirect
from scrapper import getJobs

app = Flask("SupperScrapper")

# @app.route("/")         #데코레이터(@): 바로 아래에 있는 "함수" 찾음.
# def home():
#     return "Hello! Welcome to mi casa!"

# @app.route("/<username>")      #<>:placeholder 함수에서 사용되어야함.       //dynamic url
# def contact(username):
#     return f"Hello {username} how are you doing"
@app.route("/")
def home():
        return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()     #formating
        jobs = getJobs(word)
    else:
        return redirect("/")
    return render_template("report.html",searchingBy=word)

app.run(host = "localhost")