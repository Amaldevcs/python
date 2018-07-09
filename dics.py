a = {}
a['amal'] = 12
a['sachin'] = 45
a['soman'] = 12
print a['amal']
r = []
for i in a.keys():
	 if a[i] == int(12):
        
	    r.append(i)
for t in r:
	print t
