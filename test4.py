import os
import sys
names = os.listdir(sys.argv[1])
file_path = []
for name in names:
	file_path.append (os.path.join(sys.argv[1],name))
def fun(filepath):
 name0  = []
 name2 =  []
 for paths in filepath:
      if os.path.isdir(paths):
         name0.append (paths)
      else:
                 name2.append(paths)
 print
 print "directories are",name0
 print
 print "files are: ",name2
 for i in name0:
   cont = os.listdir(i)
   rec = []
   for cont1 in cont:
     rec.append(os.path.join(i,cont1))
   print 
   print "under",i
   fun(rec)

fun(file_path)


