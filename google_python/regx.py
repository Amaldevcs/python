import re
s = "amal dev"
pat = "dev"
r = re.search(pat,s)
print r.group()

