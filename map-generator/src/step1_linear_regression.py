import json
import numpy as np
from scipy import optimize
from sklearn import linear_model

sourcePath = "../output/templateMapping/_result.txt"
data = json.load(open(sourcePath))

result = []
notesCount = len(data)

print("notesCount:")
print(notesCount)

Xs = []
Ys = []
for index in range(0, notesCount-1):
  notePositions = data[index]
  for notePosition in notePositions:
    Xarray = [0] * (notesCount + 1)
    Xarray[0] = notePosition["index"]
    Xarray[index + 1] = 1 #
    Xs.append(Xarray)
    Ys.append(notePosition["position"])

reg = linear_model.LinearRegression()
reg.fit(Xs, Ys)

print("slope:")
print(reg.coef_[0])
for i in reg.coef_:
  print(i)
'''
resultWithInterval = []
lastB = 0
for index in range(0, len(result)-1):
  interval = 0
  if lastB:
    interval = lastB - result[index]["b"]
  lastB = result[index]["b"]
  resultWithInterval.append({
    "a": result[index]["a"],
    "b": result[index]["b"],
    "interval": interval
  })
    
print(resultWithInterval)

outputPath = "../output/templateMapping/_least_sq_result.txt"
with open(outputPath, 'w') as resultFile:
  json.dump(resultWithInterval, resultFile, indent=2)
  
'''