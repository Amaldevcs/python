a = []
print "enter the limit"
j = input()
for i in range(j):
	print "enter the words"
	b = raw_input()
	a.append(b)
print a
def comma(x):
	c = []
	s = len(x)
	for i in range(s-1):
	 d = (x[i])+','+' '
         c.append(d)
	d = 'and'+' '+x[len(x)-1]
	c.append(d)
	for i in range(len(x)):
	 print c[i],          
comma(a)
 
