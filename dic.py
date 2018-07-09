a = {}
a['amal'] = 28
a['divin'] = 12
a['sachin'] = 33
a['ajay'] = 28
print a
print a.values()
j = 0
for i in a.values():
	j = j+i
print j
print a.keys()
d = a.keys()
f= a.values()
for i in a.values():
    c = d[a.values().index(i)]
    #if c:
    print c,i
    d.remove(c)    
    d.append('')
    print d

   #    d.printinsert(-1,'')
     #print a.keys()[a.values().index(i)]  
