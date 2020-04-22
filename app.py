import os
from flask import Flask, request, redirect, url_for, render_template, flash, session
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def top():
  return render_template("top.html")

@app.route("/fetch", methods=["GET","POST"])
def fetch():
  if request.method == "POST":
    if request.form["InputText"]:
      results_verb = []
      results_noun = []

      text = request.form["InputText"]
      
      token_filters = [POSKeepFilter(['名詞']), TokenCountFilter(sorted=True)]
      a = Analyzer(token_filters=token_filters)
      for k, v in a.analyze(text):
        results_verb.append([k,v])
      
      token_filters = [POSKeepFilter(['動詞']), TokenCountFilter(sorted=True)]
      a = Analyzer(token_filters=token_filters)
      for k, v in a.analyze(text):
        results_noun.append([k,v])

      return render_template("result.html", results_noun=results_noun, results_verb=results_verb)
    else:
      flash("テキストが入力されていません")
  return render_template("top.html")