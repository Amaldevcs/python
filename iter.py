class inverse:
 def __init__(self,a):
  self.n = a
  self.len = len(a)-1
 def __iter__(self):
  return self
 def next(self):
  if self.len > 0:
   i = self.n[self.len]
   self.len = self.len - 1
   return i
  else:
   raise Stopiteration()  
c=[1,2,3,4]
b =inverse(c)
print b.next()
print b.next()
print b.next()
