def print_msg(fun1):
 print "ok"
 def fun():
  print"ok ok"
  return fun1()
 return fun
@print_msg
def fun1():
 print "ok ok ok"
#fun1 = print_msg(fun1)same as the "@print_msg"
fun1()


