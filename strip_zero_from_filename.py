import os

files = os.listdir("./")

for key in range(0, len(files)):
  if files[key][0] == "0":
    os.rename(files[key], files[key].strip("0"))