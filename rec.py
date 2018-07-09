my_expr = ['+',['+',3,4],8]
def eval (expr):
	if isinstance(expr,int):
	 return expr
	else:
 	 if expr[0] == '+':
	  return expr[2] + eval(expr[1])
print eval(my_expr)

