import string
fin = open('file.txt')
for line in fin:
   line = line.strip(string.punctuation + string.whitespace)
   line  = line.upper()
   print line

