def readfile(filename):
 for file in filename:
  for lines in open(file):
    if  len(lines) > 10:
     print lines
a=[]
b=raw_input("enter the filenames")
a.append(b)
readfile(a)

