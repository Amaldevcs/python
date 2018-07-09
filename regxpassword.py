import re
print "enter the password"
p = raw_input()
def password(a):
	pat = re.compile(r'^\w.......',re.IGNORECASE)
	r = re.search(pat,a)
	if r:
		pat1 = re.compile(r'\d')
		e = re.search(pat1,a)
		if e:
			pat2 = re.compile(r'\w')
			f = re.search(pat2,a)
			if f:
		         		print "its ok"
                else:
                   print "not accepted"
	else:
	 print "not acceptaed"
password(p)

