class rational:
 def __init__(self,den,num):
  self.n = den
  self.d = num
 def __add__(self,other):
  return self.n + other.d
 def __str__(self):
  return "%s/%s" % (self.n,self.d)
a = rational(5,6)
b = rational(3,2)
print a.__str__()
print a.__add__(b)

