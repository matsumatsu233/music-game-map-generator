import cv2
import numpy as np
from matplotlib import pyplot as plt
from string import Template
import time

def getVerticalPosition(resultPositions):
  maxX = 230
  minX = 220
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

start_time = time.time()

img_path_template = Template("frames_jpg/${index}.jpg")
output_path = "output/_result.txt"

last = 4004
step = 1

with open(output_path, 'w') as result_file:
  for index in range(1,last):
    print("processing " + str(index) + "/" + str(last))

    result_file.write("-----" + str(index) + "/" + str(last) + " index: " + str(index * step) + "-----"  + "\n")

    img_path = img_path_template.substitute(index=index*step)
    img_rgb = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('yellow_note.png',0)
    w, h = template.shape[::-1]

    #result_file.write("w: " + str(w) + " h: " + str(h) + "\n")

    result = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    result_position = zip(*np.where(result >= threshold)[::-1])

    final = getVerticalPosition(result_position)
    print("final: " + str(final))
    result_file.write("final: " + str(final) + "\n")

print("--- %s seconds ---" % (time.time() - start_time))
