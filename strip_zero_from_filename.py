import os

FRAMES_JPG_DIR = "./frames_jpg/";
files = os.listdir(FRAMES_JPG_DIR)

for key in range(0, len(files)):
  if files[key][0] == "0":
    print("rename " + files[key] + " to " + files[key].strip("0"))
    os.rename(FRAMES_JPG_DIR + files[key], FRAMES_JPG_DIR + files[key].strip("0"))