import cv2
import numpy as np
from matplotlib import pyplot as plt
from string import Template
import time

def getVerticalPosition(resultPositions):
  maxX = 184
  minX = 174
  result = []
  bufferArray = []
  lastY = -20;
  for pt in resultPositions:
    X, Y = pt
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

def getRoughInterval(totalResult, firstNotEmpty):
  result = {}
  for index in range(firstNotEmpty, firstNotEmpty + 20):
    for X in range(len(totalResult[index+1])):
      for Y in range(len(totalResult[index])):
        if totalResult[index+1][X] > totalResult[index][Y]:
          sub = totalResult[index+1][X] - totalResult[index][Y]
          if sub in result:
            result[sub] +=1
          else:
            result[sub] = 1
  return max(result, key=result.get)

def printNotes(notes):
  print("notes:")
  for noteIndex in range(0, len(notes)):
    print(str(noteIndex) + ": " + str(notes[noteIndex]))

start_time = time.time()

# Get position from images
img_path_template = Template("frames_jpg/${index}.jpg")
output_path = "output/_result.txt"

total = 4004
step = 1

totalResult = []
firstNotEmpty = 0

with open(output_path, 'w') as result_file:
  for index in range(1,total):
    print("processing " + str(index) + "/" + str(total))

    img_path = img_path_template.substitute(index=index*step)
    img_rgb = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('hihat.png',0)
    w, h = template.shape[::-1]

    templateMappingresult = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    resultPositions = zip(*np.where(templateMappingresult >= threshold)[::-1])

    final = getVerticalPosition(resultPositions)
    print("final: " + str(final))
    result_file.write(" index: " + str(index * step) + " " + str(final) + "\n")
    totalResult.append(final)

    if (firstNotEmpty == 0) and final:
      firstNotEmpty = index

print(totalResult)

# Convert position data to map data

# merge position of same note into one list

roughInterval = getRoughInterval(totalResult, firstNotEmpty)
print("roughInterval " + str(roughInterval))

notes = []
current = 0
tolerance = 2
firstPositionLimitation = 50

for index in range(0, len(totalResult)):
  for notePosition in totalResult[index]:
    currentNote = (index, notePosition)
    if len(notes) == 0: # To distinguish the first time
      notes.append([currentNote])
    else:
      isOldNote = False
      for noteIndex in range(0, len(notes)):
        if abs(notePosition - notes[noteIndex][-1][1] - roughInterval) < tolerance and index == notes[noteIndex][-1][0] + 1:
          print("old note!")
          notes[noteIndex].append(currentNote)
          isOldNote = True
          break;
      if not isOldNote:
        # Too large notePosition means this note has already been recognized before
        if notePosition < firstPositionLimitation:
          print("new note!")
          notes.append([currentNote])
    print("index " + str(index) + " notePosition " + str(notePosition))
    print("------------------------------------------")

printNotes(notes)

# calculate the average interval

averageInterval = 0

for note in notes:
  interval = (note[-1][1] - note[0][1]) / (note[-1][0] - note[0][0])
  averageInterval += interval

averageInterval = averageInterval / len(notes)

print("averageInterval: " + str(averageInterval))


print("--- %s seconds ---" % (time.time() - start_time))

