import json
import numpy as np
from scipy import optimize

def leastSquare(x, y):
  A = np.vstack([x, np.ones(len(x))]).T
  m, c = np.linalg.lstsq(A, y)[0]
  print(m, c)
  return {
    "a": m,
    "b": c
  }

sourcePath = "../output/templateMapping/_result.txt"
data = json.load(open(sourcePath))

result = []
for items in data:
  X = np.array(list(map((lambda item: item["index"]), items)))
  Y = np.array(list(map((lambda item: item["position"]), items)))
  result.append(leastSquare(X, Y))

print(result)

outputPath = "../output/templateMapping/_least_sq_result.txt"
with open(outputPath, 'w') as resultFile:
  json.dump(result, resultFile, indent=2)
  
