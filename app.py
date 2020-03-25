from flask import Flask, request, redirect, url_for, render_template, flash, session

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")