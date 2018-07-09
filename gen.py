def fib(n):
	a = 0
	b = 1
	yield a
	yield b
	for i in range (n-2):
	 c = a + b 
	 yield c
	 a = b
	 b = c
a = fib(12)
for i in a:
	print i
