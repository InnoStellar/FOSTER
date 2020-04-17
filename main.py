from bottle import *
from functions import *
import urllib.request
import urllib.parse
import json
import sqlite3

@route('/')
def index():
  return static_file("foster.html", root = "")

@route('/fostercss')
def index():
  return static_file("foster.css", root = "")

@route('/fosterjs')
def index():
  return static_file("foster.css", root = "")

@route('/trainer')
def trainer():
  return static_file("trainer.html", root = "")

@route('/trainer/trainercss')
def trainer():
  return static_file("trainer.css", root = "")

@route('/trainer/trainerjs')
def trainer():
  return static_file("trainer.js", root = "")


@route('/trainee')
def trainee():
  return static_file("trainee.html", root = "")

@route('/trainee/traineecss')
def trainee():
  return static_file("trainee.css", root = "")

@route('/trainee/traineejs')
def trainee():
  return static_file("trainee.js", root = "")

@route('/thanks')
def thanks():
  return static_file("thanks.html", root = "")

@route('/match')
def match():
  return static_file("match.html", root = "")

@route('/match/matchcss')
def match():
  return static_file("match.css", root = "")

@route('/match/matchjs')
def match():
  return static_file("match.js", root = "")

@post("/trainerdata")
def trainerdata():
  content = request.body.read()
  content = content.decode()
  content_ = json.loads(content)
  addToDataBaseTrainer(content_)

@post("/traineedata")
def traineedata():
  content = request.body.read()
  content = content.decode()
  content_ = json.loads(content)
  print(content_)
  return json.dumps(addToDataBaseTrainee(content_))

@post("/fmatch")
def fmatch():
  content = request.body.read()
  content = content.decode()
  content_ = json.loads(content)

@route("/giveMatch")
def giveMatch():
  q = ""
  with open("match.json","r") as f:
    i = f.read() 
    for k in i:
      q = q + k
  print(q)
  return q

run(host='0.0.0.0',port='8080',debug=True)