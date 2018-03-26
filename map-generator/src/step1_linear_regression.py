import json
import numpy as np
from scipy import optimize
from sklearn import linear_model

sourcePath = "../output/templateMapping/_result.txt"
data = json.load(open(sourcePath))

result = []
notesCount = len(data)

Xs = []
Ys = []
for index in range(0, notesCount):
  notePositions = data[index]
  for notePosition in notePositions:
    Xarray = [0] * (notesCount + 1)
    Xarray[0] = notePosition["index"]
    Xarray[index + 1] = 1 #
    Xs.append(Xarray)
    Ys.append(notePosition["position"])

reg = linear_model.LinearRegression(fit_intercept=True)
reg.fit(Xs, Ys)

resultWithInterval = []
lastNote = 0
for index in range(1, len(reg.coef_)):
  currentNote = reg.coef_[index]
  interval = 0
  if lastNote:
    interval = lastNote - currentNote
  resultWithInterval.append({
    "index": index,
    "position": currentNote,
    "interval": interval
  })
  lastNote = currentNote

outputPath = "../output/templateMapping/_linear_regression_result.txt"
with open(outputPath, 'w') as resultFile:
  json.dump(resultWithInterval, resultFile, indent=2)
