import os
from flask import Flask, request, redirect, url_for, render_template, flash, session
from janome.tokenizer import Tokenizer

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def top():
  return render_template("top.html")

@app.route("/fetch", methods=["GET","POST"])
def fetch():
  if request.method == "POST":
    if request.form["InputText"]:
      t = Tokenizer()
      result = []
      for token in t.tokenize(request.form["InputText"]):
        result.append(token)
      return render_template("result.html", results=result)
    else:
      flash("テキストが入力されていません")
  return render_template("top.html")