import re
f = open('file.txt')
for line in f:
	#print line
        pat = r'^amal$'
        r = re.search(pat,line)
        if r:
           print r.group()

