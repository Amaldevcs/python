import re
f = open('file.txt')
for line in f:
	pat = re.compile(r'is',re.IGNORECASE)
	r= re.search(pat,line)
	if r:
	 print r.group()
	 print line

