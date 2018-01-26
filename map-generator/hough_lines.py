import cv2
import numpy as np

tolerate = 2

img = cv2.imread('frames_jpg/1069.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,250,apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)

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

    if (abs(y2 - y1) < tolerate) and (y1 < 250):
      print(str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2))
      cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',img)