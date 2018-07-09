a = {}
print "enter the no.of items"
r = input()
for i in range(r):
	print "enter the key"
	b = raw_input()
	print "enter the value"
	c = input()
	a[b] = c
def dis(s):
	print "the inventery is"
	total = 0
	for k,v in s.items():
		print k,v
		total = total + v 
	print "total number of items",total
dis(a)

