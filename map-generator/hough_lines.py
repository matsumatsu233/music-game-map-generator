import cv2
import numpy as np
from string import Template

def recognizeSectionLine(imagePath, resultIndex):
  tolerate = 2
  maxY = 250

  img = cv2.imread(imagePath)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray,50,250,apertureSize = 3)
  lines = cv2.HoughLines(edges,1,np.pi/180,150)

  for index in range(0, len(lines)-1):
    for rho,theta in lines[index]:
      a = np.cos(theta)
      b = np.sin(theta)
      x0 = a*rho
      y0 = b*rho
      x1 = int(x0 + 1000*(-b))
      y1 = int(y0 + 1000*(a))
      x2 = int(x0 - 1000*(-b))
      y2 = int(y0 - 1000*(a))

      if (abs(y2 - y1) < tolerate) and (y1 < maxY):
        print(str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
  cv2.imwrite('result' + str(resultIndex) + '.jpg', img)

start = 1000
end = 1100
step = 1

imgPathTemplate = Template("frames_jpg/${index}.jpg")

for index in range(start, end):
  print("processing " + str(index - start) + "/" + str(end - start))

  imgPath = imgPathTemplate.substitute(index=index*step)
  recognizeSectionLine(imgPath, index)