import sqlite3
import json

def writeToFile(match):
  match = json.dumps(match)
  with open("match.json","w") as f:
    f.write(match)

def addToDataBaseTrainer(fields):
  fields = tuple(fields)
  conn = sqlite3.connect('dataOfClients.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS trainer(name,email,AvgK, NumFk,NumMk,Num, Loc, EthP, EthK)''')
  c.execute("INSERT INTO trainer VALUES (?,?,?,?,?,?,?,?,?)",fields)
  conn.commit()
  conn.close

def addToDataBaseTrainee(fields):
  fields = tuple(fields)
  print(fields)
  conn = sqlite3.connect('dataOfClients.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS trainee(name,email,AvgK,NumFk,NumMk,Num,Loc,EthP,Ethk)''')
  c.execute("INSERT INTO trainee VALUES (?,?,?,?,?,?,?,?,?)",fields)
  i = findMatch(list(fields))
  writeToFile(i)
  conn.commit()
  conn.close
  

def getpermatch(trainee, trainer):
  q = 0
  for i in range(2 , len(trainee)):
    if trainee[i]  == trainer[0]:
      q = q + 1
  return (q/(len(trainee) - 2))*100


def findMatch(fields):
  per = 0
  conn = sqlite3.connect('dataOfClients.db')
  c = conn.cursor()
  row = c.execute("SELECT * FROM trainer")
  for i in row:
    if per < getpermatch(fields, i):
      per = getpermatch(fields, i)
      traineremail = i
      print(per)
  return {i[0]:[per,i]}
    

  
  

  
