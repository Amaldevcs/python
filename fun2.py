def sqr():
     return lambda x: x*x
def cube():
     return lambda x: x*x*x
def differntial(f,x):
     return (f(x+0.000001) - f(x))/0.000001
print "enter the sqr value"
a = input()
print "cube value"
b = input()
print differntial(sqr(),a)
print differntial(cube(),b)


