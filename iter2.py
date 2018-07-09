class fib:
 def __init__(self):
  self.i = 0
  self .j = 1
 def __iter__(self):
  return self
 def next (self):
  print self.i
  self.k = self.i + self.j
  self.i =self.j
  self.j =self.k
b = fib()
for i in range(10):
 b.next() 
