import cv2
import numpy as np
from matplotlib import pyplot as plt
from string import Template

img_path_template = Template("frames_jpg/${index}.jpg")
output_path_template = Template("output/result${index}.png")

for index in range(1,100):
  print("processing " + str(index) + "/100")
  img_path = img_path_template.substitute(index=index*40)
  img_rgb = cv2.imread(img_path)
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  template = cv2.imread('yellow_note.png',0)
  w, h = template.shape[::-1]

  res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
  threshold = 0.8
  loc = np.where( res >= threshold)
  for pt in zip(*loc[::-1]):
      cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

  output_path = output_path_template.substitute(index=index*40)
  cv2.imwrite(output_path,img_rgb)
