import os
import sys
arr = os.listdir(sys.argv[1])
for j in arr:
	print j
size = {}
for i in arr:
	statinfo = os.stat(sys.argv[1]+'/'+i)
	size[i] = statinfo.st_size
#print size
r = []
a = size.values()
a.sort(reverse=True)
pp = {}
p = 0
for i in a:
	for keyword in size.keys():
		if size[keyword] == i:
			 pp[keyword] = i
			 #r.append(keyword)
                         
for keyword in pp.keys():
		print keyword,pp[keyword] 

		 
print len(a)
print len(r)


