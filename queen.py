partial ="1425"
col =8
def check(partial,col):
 row = len(partial)
 if partial:
  spread = 1
  for prow in range(row-1,-1,-1):
   if int(partial[prow]) in (col,col-spread,col+spread):
    return False
   spread+=1
 return True
print check(partial,col)

