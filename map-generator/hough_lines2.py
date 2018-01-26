import cv2
import numpy as np

img = cv2.imread('frames_jpg/1069.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('houghlines_gray.jpg', gray)

edges = cv2.Canny(gray,50,250,apertureSize = 3)
cv2.imwrite('houghlines_edges.jpg', edges)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for index in range(0, len(lines)-1):
  for x1,y1,x2,y2 in lines[index]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)