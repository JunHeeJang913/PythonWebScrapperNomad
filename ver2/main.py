from flask import Flask, render_template, request, redirect, send_file
from scrapper import getJobs
from export import saveToFile
app = Flask("SupperScrapper")

# @app.route("/")         #데코레이터(@): 바로 아래에 있는 "함수" 찾음.
# def home():
#     return "Hello! Welcome to mi casa!"

# @app.route("/<username>")      #<>:placeholder 함수에서 사용되어야함.       //dynamic url
# def contact(username):
#     return f"Hello {username} how are you doing"

db = {}

@app.route("/")
def home():
        return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()     #formating
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = getJobs(word)   
            db[word]=jobs
    else:
        return redirect("/")
    return render_template("report.html",searchingBy=word,resultsNumeber = len(jobs), jobs = jobs)

@app.route("/export")
def export():
    try: 
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:    #db에 없으면
            raise Exception()
        saveToFile(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")
      

app.run(host = "localhost")