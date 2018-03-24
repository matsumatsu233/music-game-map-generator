import json
import cv2
import numpy as np
from string import Template

def getVerticalPosition(resultPositions):
  maxX = 230
  minX = 220
  result = []
  bufferArray = []
  lastY = -20
  for pt in resultPositions:
    X, Y = pt
    X, Y = X.item(), Y.item()
    if (X > minX) and (X < maxX):
      if (Y - lastY >= 2):
        if len(bufferArray) > 0:
          middleIndex = int((len(bufferArray)-1)/2)
          result.append(bufferArray[middleIndex])
          bufferArray = []
      else:
        bufferArray.append(Y)
      lastY = Y
  if len(bufferArray) > 0:
    result.append(bufferArray[int((len(bufferArray)-1)/2)])
  return result


# Get position from images
imgPathTemplate = Template("../input/frames_jpg/${index}.jpg")
outputPath = "../output/templateMapping/_result.txt"

total = 4004
step = 1

totalResult = []
jsonResult = []
firstNotEmpty = 0

with open(outputPath, 'w') as resultFile:
  for index in range(1,total):
    print("processing " + str(index) + "/" + str(total))

    imgPath = imgPathTemplate.substitute(index=index*step)
    imgGray = cv2.cvtColor(cv2.imread(imgPath), cv2.COLOR_BGR2GRAY)
    template = cv2.imread('../input/yellow_note.png',0)
    w, h = template.shape[::-1]

    templateMappingresult = cv2.matchTemplate(imgGray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    resultPositions = zip(*np.where(templateMappingresult >= threshold)[::-1])

    result = getVerticalPosition(resultPositions)
    jsonResult.append({
      "snare": result
    })
    print("result: " + str(result))
    #resultFile.write(" index: " + str(index * step) + " " + str(final) + "\n")

    # TODO is this useful?
    if (firstNotEmpty == 0) and result:
      firstNotEmpty = index
  
  print(jsonResult)
  json.dump(jsonResult, resultFile, indent=2)
