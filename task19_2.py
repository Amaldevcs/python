#all files that end with:" .py " in a given directory?
import re
import os
import sys
names = os.listdir(sys.argv[1])
print names
filepath = []
for name in names:
 filepath.append(os.path.join(sys.argv[1],name))
print filepath
files = []
for path in  filepath:
 if os.path.isfile(path):
  files.append(path)
for path in files:
    pat = r'.py$'
    r = re.search(pat,path)
    if r:
     print path


 


